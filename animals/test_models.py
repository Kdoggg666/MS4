from django.test import TestCase
from .models import Category, Animal


class TestModels(TestCase):
    """
    Tests for animals app models.
    """
    def test_animal_string_method_returns_name(self):
        animal = Animal.objects.create(name='Ball Python1', price=49.99)
        self.assertEqual(str(animal), 'Ball Python1')

    def test_category_string_method_returns_name(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(str(category), 'Test Category')
