from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from animals.models import Animal, Category
from .models import Care
from .forms import CareForm


def all_animals_care(request):
    """
    A view to show all animal care guides, including sorting and search queries
    """
    animals = Animal.objects.all()
    care = Care.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                animals = animals.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            animals = animals.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            animals = animals.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('animals'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            animals = animals.filter(queries)
    objects_list = list(zip(animals, care))
    current_sorting = f'{sort}_{direction}'
    #  Pagination from Django docs.
    paginator = Paginator(objects_list, 6)  # Show 6 results per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'animals': animals,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'page_obj': page_obj,
        'care': care,
        'objects_list': objects_list,
    }

    return render(request, 'care/care.html', context)


def animal_care(request, animal_id):
    """
    View for Animal Care.
    """
    animal = get_object_or_404(Animal, pk=animal_id)
    care = get_object_or_404(Care, pk=animal_id)

    context = {
        'animal': animal,
        'care': care,
    }
    return render(request, 'care/care_details.html', context)


@login_required
def add_care(request):
    """ Add an care guide to animal """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CareForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save()
            messages.success(request, 'Successfully added Care guide!')
            return redirect(reverse('animal_care', args=[animal.id]))
        else:
            messages.error(request,
                           'Failed to add care guide. Please ensure the form is \
                           valid.')
    else:
        form = CareForm()

    template = 'care/add_care.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_care(request, animal_id):
    """ Edit an care guide """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admins can do that.')
        return redirect(reverse('home'))

    care = get_object_or_404(Care, pk=animal_id)
    animal = get_object_or_404(Animal, pk=animal_id)

    if request.method == 'POST':
        form = CareForm(request.POST, request.FILES, instance=care)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated care guide!')
            return redirect(reverse('animal_care', args=[animal.id]))
        else:
            messages.error(request, 'Failed to update care guide. Please ensure \
                           the form is valid.')
    else:
        form = CareForm(instance=care)
        messages.info(request, f'You are editing {care.name}')

    template = 'care/edit_care.html'
    context = {
        'form': form,
        'animal': animal,
        'care': care,
    }

    return render(request, template, context)
