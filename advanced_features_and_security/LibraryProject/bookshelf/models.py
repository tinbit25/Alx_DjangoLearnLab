from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        """
        Create and return a regular user with an email, username, date_of_birth, and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)  # Normalize the email
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)  # Ensure password is hashed
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        """
        Create and return a superuser with email, username, date_of_birth, and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, email, date_of_birth, password, **extra_fields)


# Custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()  # Link Custom User Manager

    def __str__(self):
        return self.username
