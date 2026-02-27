from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.patients.urls')),
    path('api/', include('hospital.urls')),
]
