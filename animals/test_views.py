from django.test import TestCase
from .models import Animal


class TestViews(TestCase):
    """
    Tests for animals app views.
    """
    def test_animals_page(self):
        response = self.client.get('/animals/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animals/animals.html')

    def test_animals_page_filter(self):
        animal = Animal.objects.create(name='Test Animal', price=99.99)
        response = self.client.get(f'/animals/{animal.name}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animals/animals.html')    
