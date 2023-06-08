from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login_system', views.login_system, name='login_system'),
    path('all_data', views.all_data, name='all_data'),
    path('create', views.create, name='create')
]
