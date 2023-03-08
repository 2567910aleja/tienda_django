from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('inventario', include('inventario.urls')),
    path('admin/', admin.site.urls),
]
