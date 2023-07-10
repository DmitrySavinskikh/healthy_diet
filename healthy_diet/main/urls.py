from django.urls import path
from . import views
from login_system import views as views_log_syst


urlpatterns = [
    path('', views.index, name='home'),
    path('sugar_counting', views.sugar_counting, name='sugar_counting'),
    path('login_system', views_log_syst.goto_firstpage, name='login_system'),
    path('all_data', views.all_data, name='all_data'),
    path('create', views.create, name='create'),
]
