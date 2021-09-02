import json

from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField


class Domain(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    domain_access = JSONField()
    current_domain = models.ForeignKey(Domain, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def pretty_domain_access(self):
        return json.dumps(self.domain_access, indent=4)


class Product(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
