from django.db import models

# Create your models here.
class Userform(models.Model):
    username = models.CharField(max_length=50, default=" ")
    email = models.EmailField(default=" ")
    password = models.CharField(max_length=50, default=" ")
    city = models.CharField(max_length=50, default=" ")
    phone_no = models.CharField(max_length=10, default=" ")
    dob = models.DateField(null=True, blank=True)