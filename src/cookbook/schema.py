import graphene
from cookbook.models import Ingredient, Recipe, Tag
from cookbook.types import IngredientType, RecipeType, TagType


def _params_to_ints(qs):
    """Convert a list of string IDs to a list of integers"""
    return [int(str_id) for str_id in qs.split(',')]


class CookBookQuery(graphene.ObjectType):

    all_recipe = graphene.List(
        RecipeType,
        tags=graphene.String(
            required=False
        ),
        ingredients=graphene.String(
            required=False
        ),
        description="It shows all the recipes on database by default. \
            You can filter by tags id's (separated by commas) and/or \
            ingredients id's (separated by commas)"
        )
    all_ingredients = graphene.List(
        IngredientType,
        assignedOnly=graphene.Boolean(
            default_value=False
            ),
        description="It shows all the ingredients on database by default. \
            You can filter only to check the assigned ingredients to a \
            recipe"
        )
    all_tags = graphene.List(
        TagType,
        assignedOnly=graphene.Boolean(
            default_value=False
            ),
        description="It shows all the tags on database by default. \
            You can filter only to check the assigned tags to a \
            recipe"
        )
    ingredients_by_name = graphene.Field(
        IngredientType,
        name=graphene.String(
            required=True
            ),
        description=("It search an ingredient by name (case insensitive)")
        )
    tag_by_name = graphene.Field(
        TagType,
        name=graphene.String(
            required=True
            ),
        description=("It search a tag by name  (case insensitive)")
        )

    def resolve_all_recipe(root, info, tags=None, ingredients=None):
        myquery = Recipe.objects.all()
        if tags:
            tags_ids = _params_to_ints(tags)
            myquery = myquery.filter(tags__id__in=tags_ids)
        if ingredients:
            ingredients_ids = _params_to_ints(ingredients)
            myquery = myquery.filter(ingredients__id__in=ingredients_ids)
        return myquery

    def resolve_all_ingredients(root, info, assignedOnly):
        if not assignedOnly:
            return Ingredient.objects.all()
        return Ingredient.objects.filter(
            recipe__isnull=False).order_by('id').distinct()

    def resolve_all_tags(root, info, assignedOnly):
        if not assignedOnly:
            return Tag.objects.all()
        return Tag.objects.filter(
            recipe__isnull=False).order_by('id').distinct()

    def resolve_ingredients_by_name(root, info, name):
        try:
            return Ingredient.objects.get(name__iexact=name)
        except Ingredient.DoesNotExist:
            return None

    def resolve_tag_by_name(root, info, name):
        try:
            return Tag.objects.get(name__iexact=name)
        except Tag.DoesNotExist:
            return None

    class Meta:
        description = "This Query manage a cookbook database with recipes \
            and the ingredients than contains them. The recipes can be \
            cataloged with tags."


schema = graphene.Schema(query=CookBookQuery)
