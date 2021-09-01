from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resource_permissions = JSONField()


class Product(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
