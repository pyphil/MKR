from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=32)


class AllowedEmail(models.Model):
    emails = models.TextField()
    school = models.CharField(max_length=100)


class Config(models.Model):
    NAME_CHOICES = [
        ('noreply-mail', 'noreply-E-Mail-Absenderadresse zum Versand der Codes'),
        ('mail_text', 'Mailtext zum Versand der Codes'),
    ]
    name = models.CharField(max_length=50, choices=NAME_CHOICES)
    setting = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.setting
