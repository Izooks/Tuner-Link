from bisect import bisect_right
from distutils.command.upload import upload
import email
from pickle import TRUE
from tkinter import CASCADE
from types import CoroutineType
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import PasswordInput
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, null=False, default="Name")
    email = models.CharField(max_length=200, null=False, default="Email")
    dob = models.DateField(auto_now_add=False, null=True)
    city = models.CharField(max_length=200, null=False, default="City")
    image = models.ImageField(null=False, default="subie.jpg", upload_to="images/")
    description = models.TextField(null=False, default="Description")
    car = models.CharField(max_length=200, null=False, default="Car")
    modifications = models.TextField(null=False, default="Mods")

    def __str__(self):
        return self.name


