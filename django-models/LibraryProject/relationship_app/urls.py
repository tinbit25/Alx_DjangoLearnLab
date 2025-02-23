from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
]


from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # Assuming you have a function-based register view
]
