from django.test import TestCase
from .models import Animal
from .views import all_animals, animal_details, all_animals_care, animal_care


class TestViews(TestCase):
    """
    Tests for animals app views.
    """
    def test_animals_page(self):
        response = self.client.get('/animals/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animals/animals.html')

    def test_animal_details(self):  # Fix this 
        response = self.client.get('/animals/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animals/animal_details.html')

    def test_care_page(self): # Fix this
        response = self.client.get('animals/care/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animals/care.html')

    def test_care_details(self): # Fix this
        response = self.client.get('animals/care/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animals/care_details.html')
