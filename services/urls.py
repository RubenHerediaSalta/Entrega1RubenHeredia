from django.urls import path
from services.views import *


urlpatterns = [
    
    path('create-services', create_services),
    path('list-services', list_services),
]