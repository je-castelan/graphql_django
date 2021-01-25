Graphene testing
================

Created by: Jose Emanuel Castelan

This repository has my testings and knowledge about Graph applied to Python and Django using Graphene library.

You can check my project code on [the cookbook app](src/cookbook).

# How to install

 - Clone the git repository
 - Build the project

> docker-compose build

 - Run the project

>  docker-compose up

 - Enter to `localhost:8000/graphql/` to check the GraphiQL and check API doc and run the queries.

 - If you want it, you can add a superuser with the following command to try to enter to admin interface on `localhost:8000/admin/`

> docker-compose run --rm app_graph sh -c "python manage.py createsuperuser"

 - In case to check testing executed, you can run the following command

> docker-compose run --rm app_graph sh -c "python manage.py test && flake8"