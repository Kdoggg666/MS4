from django import forms
from animals.models import Animal, Category
from .models import Care


class CareForm(forms.ModelForm):

    class Meta:
        model = Care
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        animals = Animal.objects.all()
        care = Care.objects.all()
