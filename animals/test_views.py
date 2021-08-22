from django.test import TestCase


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
