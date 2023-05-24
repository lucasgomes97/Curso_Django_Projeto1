from django.urls import path

from recipes.views import home

# dominio/recipes/sobre
urlpatterns = [
    path('', home),
]
