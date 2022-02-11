#Users Models
#Django
from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    #Profile Model
    #Proxy model that extends the base dta with other information
    
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
        )
    first_name=models.CharField(max_length=20, blank=True)
    last_name=models.CharField(max_length=20, blank=True)
    email=models.CharField(max_length=50, blank=True)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)    

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now=True)
    modified= models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.user.username
    #return Username






"""
Una forma de crear un modelo de usuario usando ORM

from venv import create
from django.db import models
from django.forms import PasswordInput

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)    
    bio = models.TextField(max_length=200, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
"""
