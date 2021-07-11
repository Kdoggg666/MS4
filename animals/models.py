from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Category class.
    """
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Animal(models.Model):
    """
    Animal class.
    """
    name = models.CharField(max_length=30)
    latin_name = models.CharField(max_length=30)
    climate = models.CharField(max_length=30)
    min_tank_size = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
