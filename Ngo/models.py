from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, default='No description')
    place = models.CharField(max_length=50, default='Raipur')
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone Number must be 9 to 12 digits")
    contact = models.IntegerField(max_length=10)
    def __str__(self):
        return str(self.title)
