from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('productos', include('productos.urls')),
    path('admin/', admin.site.urls),
]
