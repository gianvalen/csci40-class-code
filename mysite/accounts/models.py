from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #CASCADE - to also delete the user. 
    year_level = models.IntegerField()
    course = models.CharField(max_length=10)