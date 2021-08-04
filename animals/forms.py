from django import forms
from .models import Animal, Category, Rating, Care


class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['title', 'content', 'rating_out_of_five']
        labels = {
            'title': 'Review Name',
            'content': 'Write your review here',
            'animal': 'Animal Name',
            'rating_out_of_five': 'Rate this animal from 1 to 5'

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        animals = Animal.objects.all()


class CareForm(forms.ModelForm):

    class Meta:
        model = Care
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        animals = Animal.objects.all()
        care = Care.objects.all()
