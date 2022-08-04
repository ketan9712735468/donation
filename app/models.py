from xmlrpc.client import TRANSPORT_ERROR
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


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=10)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.full_name


class Donor(models.Model):
    value = models.IntegerField()
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.value}"


GENDER_CHOICES = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
    ("OTHER", "OTHER")
)

class ForOrgans(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=6,choices = GENDER_CHOICES)
    blood_group = models.CharField(max_length=100)
    emergency_number = models.CharField(max_length=100)
    emergency_address = models.CharField(max_length=100)
    identity_card = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    organs = models.JSONField()
    tissue = models.JSONField()


class Sponsore(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='sponsore/')
    location = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Blog(models.Model):
    heading = models.CharField(max_length=250, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog/')
    date = models.DateField(auto_now=True)


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')