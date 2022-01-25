from venv import create
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=200, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

