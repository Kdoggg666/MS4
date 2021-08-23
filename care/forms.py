from django import forms
from .models import Care


class CareForm(forms.ModelForm):

    class Meta:
        model = Care
        fields = '__all__'
        labels = {
                'name': 'Animal Name',
                'care_guide': 'General Care',
                'cage_setup': 'Housing Requirements',
                'lighting': 'Lighting Requirements',
                'heating': 'Heating Requirements',
                'feeding_schedule': 'Feeding Requirements',
                'known_problems': 'Known Health Issues',
                'other_information': 'Further Reading URL',
                'other_information_name': 'Further Reading Name',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
