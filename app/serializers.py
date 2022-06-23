from app.models import BecomeVolunteer, Contact, Donor, OurVolunteers, Slider
from rest_framework import serializers


class BecomeVolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecomeVolunteer
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class OurVolunteersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurVolunteers
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'