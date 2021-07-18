from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Category class.
    """
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Animal(models.Model):
    """
    Animal class.
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    animal_id = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=30)
    latin_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30, default="")
    climate = models.CharField(max_length=30)
    temperament = models.CharField(max_length=50, default="")
    food = models.CharField(max_length=50, default="")
    min_tank_size = models.CharField(max_length=30)
    max_length = models.CharField(max_length=30, default="")
    lifespan = models.CharField(max_length=30, default="")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    temperature = models.CharField(max_length=30, default="")
    care_guide = models.TextField()
    cage_setup = models.TextField()
    lighting = models.TextField()
    heating = models.TextField()
    feeding_schedule = models.TextField()
    known_problems = models.TextField()
    other_information = models.TextField()
    other_information_name = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name
