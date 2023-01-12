from django.urls import path
from featured.views import *


urlpatterns = [
    
    path('create-featured', create_featured),
    path('list-featured', list_featured),
]