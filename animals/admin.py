from django.contrib import admin
from .models import Animal, Category, Rating, Care

# Register your models here.
admin.site.register(Animal)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Care)
