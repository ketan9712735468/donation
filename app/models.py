from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BecomeVolunteer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    number = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    occupation = models.CharField(max_length=200)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.full_name

class Slider(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.name


class OurVolunteers(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='volunteers/')

    def __str__(self):
        return self.name