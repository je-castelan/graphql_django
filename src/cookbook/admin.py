from django.contrib import admin
from cookbook.models import Ingredient, Recipe, Tag

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Tag)
