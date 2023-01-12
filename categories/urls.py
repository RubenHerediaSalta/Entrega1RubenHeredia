from django.urls import path
from categories.views import *


urlpatterns = [
    
    path('create-categories', create_categories),
    path('list-categories', list_categories),
]