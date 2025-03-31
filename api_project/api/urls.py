from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes registered with the router
]

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

