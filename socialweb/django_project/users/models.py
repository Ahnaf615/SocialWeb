from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(default="img", max_length=200)

    def __str__(self):
        return f'{self.user.username}Profile'

    def save(self, *args, **kawrgs):  # why is it used?#
        super().save(*args, **kawrgs)


