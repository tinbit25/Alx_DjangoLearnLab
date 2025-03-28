from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),  # This includes the blog's URLs
    path("accounts/", include("django.contrib.auth.urls")),  # Django auth views
]
