from django.test import TestCase

from cookbook.models import Ingredient, Tag, Recipe


class TestIngredient(TestCase):

    def test_ingredient(self):
        data = {
            "name": "Milk",
            "description": "Natural Cow Milk"
        }
        ingredient = Ingredient.objects.create(**data)
        self.assertEqual(ingredient.name, data["name"])


class TestTag(TestCase):

    def test_tag(self):
        data = {
            "name": "Breakfast",
        }
        tag = Tag.objects.create(**data)
        self.assertEqual(tag.name, data["name"])


class TestRecipe(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="Entrance")
        self.ingredients = []
        self.ingredients.append(Ingredient.objects.create(
            name="Chicken wings",
            description="Chicken wings cut on 3 parts"))
        self.ingredients.append(Ingredient.objects.create(
            name="Buffalo sauce",
            description="Prefered Hunt's"))

    def test_recipe(self):
        data = {
            "name": "Buffalo wings",
            "portions": 3,
            "recipe_steps": "Lorem itsum",
        }
        recipe = Recipe.objects.create(**data)
        recipe.tags.add(self.tag)
        for ingredient in self.ingredients:
            recipe.ingredients.add(ingredient)
        recipe.save()
        recipe.refresh_from_db()
        self.assertEqual(recipe.name, data["name"])
        self.assertEqual(len(recipe.ingredients.all()), 2)
        self.assertEqual(recipe.tags.all()[0].name, self.tag.name)
