from django.db import models
from django.contrib.auth.models import User

class Regevent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.CharField(max_length=1000)
