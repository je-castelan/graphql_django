Qraphene quick steps
====================

1.- Create models

2.- Create `DjangoObjectType` objects (seems like forms or serializers) importing from `graphene_django`

3.- Create Query inheriting from `graphene.ObjectType` importing from graphene.

Query will content the resolvers with the valid queries



4.- On Query file, create schema 

> schema = graphene.Schema(query=Query)

5.- On URL file, add graphql path

```
urlpatterns = [
    ...
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
```