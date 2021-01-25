from graphene_django import DjangoObjectType
from cookbook.models import Ingredient, Recipe, Tag


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "description",)
        description = "It shows the id, name and description of \
            an ingredient"


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "portions",
            "ingredients",
            "tags",
            "recipe_steps",
            )
        description = "It shows the information about a recipe. This \
            information has an id, the recipes name, the partions \
            to serve, the instructions, the ingredients to use and \
            the tags associated"


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ('id', 'name', )
        description = "It shows the id and name of a tag"
