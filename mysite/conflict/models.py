from django.db import models
from django.contrib.auth.models import User

""" Extending the user default model and adding some extra fields
    Also enforcing some of the rules in the fields """


class User_mod(models.Model):
    user = models.OneToOneField(User)
    reason = models.CharField(max_length = 1000)
    decision = models.BooleanField(default = False)

# Create your models here.
