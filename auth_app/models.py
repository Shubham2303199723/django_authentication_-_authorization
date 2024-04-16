from django.db import models

# Create your models here.
class Userform(models.Model):
    name = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    password = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    phone_no = models.CharField(max_length=10, default=None)
    dob = models.DateField(default=None)