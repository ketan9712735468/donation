from app.models import BecomeVolunteer, OurVolunteers, Slider
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
