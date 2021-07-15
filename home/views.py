from django.shortcuts import render
from animals.views import all_animals


def index(request):
    """
    View for index page.
    """
    return render(request, 'home/index.html')
