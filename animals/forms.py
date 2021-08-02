from django import forms
from .models import Animal, Category, Rating


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
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        animals = Animal.objects.all()
