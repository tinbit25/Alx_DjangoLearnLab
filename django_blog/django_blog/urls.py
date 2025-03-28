from django.contrib import admin
from django.urls import path
from . import views  # Ensure you import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line for the root URL
]
