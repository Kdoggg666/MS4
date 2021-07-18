from django import forms
from .models import Animal, Category


class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()

