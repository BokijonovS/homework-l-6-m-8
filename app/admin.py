from django.contrib import admin

# Register your models here.
from .models import FoodType, Food, Comment

admin.site.register(FoodType)
admin.site.register(Food)
admin.site.register(Comment)
