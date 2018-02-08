from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Type(models.Model):
    CHOICES = (
        ('Volunteer', 'VOLUNTEER'),
        ('Ngo', 'NGO'),
        ('Funder', 'FUNDER'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    RegisterAs = models.CharField(max_length=25, choices=CHOICES, default='Volunteer')

