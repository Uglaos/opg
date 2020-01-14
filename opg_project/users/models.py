from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, null=True)
    surname = models.CharField(max_length=32, null=True)
    opg_name = models.CharField(max_length=64, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=25, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
