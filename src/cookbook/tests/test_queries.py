import json

from graphene_django.utils.testing import GraphQLTestCase
from cookbook.models import Ingredient, Tag, Recipe


class IngredientQueryTestCase(GraphQLTestCase):

    def setUp(self):
        self.ingredients = []
        self.ingredients.append(Ingredient.objects.create(
            name="Chicken wings",
            description="Chicken wings cut on 3 parts"))
        self.ingredients.append(Ingredient.objects.create(
            name="Buffalo sauce",
            description="Prefered Hunt's"))

    def test_ingredient_general_query(self):
        response = self.query(
            '''
            query {
                allIngredients {
                    id
                    name
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        ingredients = content["data"]["allIngredients"]
        self.assertEqual(len(ingredients), 2)

    def test_ingredient_search_by_name(self):
        response = self.query(
            '''
            query {
                ingredientsByName (name: "buffalo sauce") {
                    id
                    name
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        ingredients = content["data"]["ingredientsByName"]
        self.assertEqual(ingredients["name"], "Buffalo sauce")


class TagQueryTestCase(GraphQLTestCase):

    def setUp(self):
        self.tags = []
        self.tags.append(Tag.objects.create(
            name="Soup"))
        self.tags.append(Tag.objects.create(
            name="Salads"))
        self.tags.append(Tag.objects.create(
            name="Desserts"))

    def test_tag_general_query(self):
        response = self.query(
            '''
            query {
                allTags {
                    id
                    name
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        tags = content["data"]["allTags"]
        self.assertEqual(len(tags), 3)

    def test_tags_search_by_name(self):
        response = self.query(
            '''
            query {
                tagByName (name: "sALADS") {
                    id
                    name
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        ingredients = content["data"]["tagByName"]
        self.assertEqual(ingredients["name"], "Salads")


class RecipeTest(GraphQLTestCase):

    def setUp(self):
        self.soup_tag = Tag.objects.create(
            name="Soup")
        self.salad_tag = Tag.objects.create(
            name="Salads")
        self.entrance_tag = Tag.objects.create(
            name="Entrance")

        self.wings_ing = Ingredient.objects.create(
            name="Chicken wings",
            description="Chicken wings cut on 3 parts")
        self.bufsauce_ing = Ingredient.objects.create(
            name="Buffalo sauce",
            description="Prefered Hunt's")
        self.tomato = Ingredient.objects.create(
            name="Tomato", description="Tomato"
        )
        self.water = Ingredient.objects.create(
            name="Water", description="Water"
        )
        Ingredient.objects.create(
            name="abc", description="def"
        )

        self.buffalo_wings = Recipe.objects.create(
            name="Buffalo wings",
            portions=3,
            recipe_steps="1,2,3"
        )

        self.buffalo_wings.tags.add(self.entrance_tag)
        self.buffalo_wings.ingredients.add(self.wings_ing)
        self.buffalo_wings.ingredients.add(self.bufsauce_ing)

        self.tomato_soup = Recipe.objects.create(
            name="Tomato soup",
            portions=1,
            recipe_steps="a,b,c"
        )

        self.tomato_soup.tags.add(self.soup_tag)
        self.tomato_soup.ingredients.add(self.tomato)
        self.tomato_soup.ingredients.add(self.water)

    def test_all_recipes(self):
        response = self.query(
            '''
            query {
                allRecipe {
                    id,
                    name,
                    portions,
                    recipeSteps,
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        tags = content["data"]["allRecipe"]
        self.assertEqual(len(tags), 2)

    def test_all_recipes_filtering_tag(self):
        response = self.query(
            '''
            query {
                allRecipe (tags: "1") {
                    id,
                    name,
                    portions,
                    recipeSteps,
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        tags = content["data"]["allRecipe"]
        self.assertEqual(len(tags), 1)

        response = self.query(
            '''
            query {
                allRecipe (tags: "1,3") {
                    id,
                    name,
                    portions,
                    recipeSteps,
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        tags = content["data"]["allRecipe"]
        self.assertEqual(len(tags), 2)

    def test_all_recipes_filtering_ingredients(self):
        response = self.query(
            '''
            query {
                allRecipe (ingredients: "1") {
                    id,
                    name,
                    portions,
                    recipeSteps,
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        tags = content["data"]["allRecipe"]
        self.assertEqual(len(tags), 1)

        response = self.query(
            '''
            query {
                allRecipe (ingredients: "1,4") {
                    id,
                    name,
                    portions,
                    recipeSteps,
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        tags = content["data"]["allRecipe"]
        self.assertEqual(len(tags), 2)

    def test_tags_assigned(self):
        response = self.query(
            '''
            query {
                allTags (assignedOnly: true) {
                    id
                    name
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        tags = content["data"]["allTags"]
        self.assertEqual(len(tags), 2)

    def test_ingredients_assigned(self):
        response = self.query(
            '''
            query {
                allIngredients (assignedOnly: true) {
                    id
                    name
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        tags = content["data"]["allIngredients"]
        self.assertEqual(len(tags), 4)
