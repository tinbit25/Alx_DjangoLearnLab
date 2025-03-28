# users/models.py
from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username
