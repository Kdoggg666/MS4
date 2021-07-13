from django.test import TestCase


class TestViews(TestCase):
    """
    Tests for animals app views.
    """
    def test_animals_page(self):
        response = self.client.get('/animals/')
        self.assertEqual(response.status_code, 200)
