from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=32)


class AllowedEmail(models.Model):
    emails = models.TextField()
    school = models.CharField(max_length=100)
