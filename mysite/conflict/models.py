from django.db import models
from django.contrib.auth.models import User

""" Extending the user default model and adding some extra fields
    Also enforcing some of the rules in the fields """


class User_mod(models.Model):
    user = models.OneToOneField(User)
    zipcode = models.FloatField(blank=False, default=00000)
    address = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
