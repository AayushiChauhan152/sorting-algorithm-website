from django.urls import path
from .views import home, generate_random_values, sort_values

urlpatterns = [
    path('', home, name='home'),
    path('generate/', generate_random_values, name='generate_random_values'),
    path('sort/', sort_values, name='sort_values'),
]
