from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login_system/', include('django.contrib.auth.urls')),
    path('login_system/', include('login_system.urls'))
]
