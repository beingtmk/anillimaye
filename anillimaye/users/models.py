from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    website = models.CharField(max_length=20, blank=True)
    message = models.TextField(max_length=500)

    def __str__(self):
        return '%s' % (self.query)

class Newsletter(models.Model):
    email = models.CharField(max_length=15)

    def __str__(self):
        return '%s' % (self.query)
