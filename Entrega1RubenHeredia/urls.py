from django.contrib import admin
from django.urls import path, include
from Entrega1RubenHeredia.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('services/', include('services.urls')),
    path('categories/', include('categories.urls')),
    path('featured/', include('featured.urls')),

]
