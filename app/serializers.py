from rest_framework import serializers
from app.models import BecomeVolunteer, Blog, Contact, Donor, ForOrgans, Gallery, OurVolunteers, Slider, Sponsore


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


ORGANS_CHOICES = (
    ("Heart", "Heart"),
    ("Lungs", "Lungs"),
    ("Kidneys", "Kidneys"),
    ("Liver", "Liver"),
    ("Pancreas", "Pancreas"),
    ("Intestine", "Intestine"),
    ("All", "All"),
)

TISSUES_CHOICES = (
    ("Corneas/Eye Balls", "Corneas/Eye Balls"),
    ("Skin", "Skin"),
    ("Bones", "Bones"),
    ("Heart Valves", "Heart Valves"),
    ("Blood Valves", "Blood Valves"),
    ("All", "All"),
)
class ForOrgansSerializer(serializers.ModelSerializer):
    # organs = serializers.MultipleChoiceField(
    #     choices=ORGANS_CHOICES)
    # tissue = serializers.MultipleChoiceField(
    #     choices=TISSUES_CHOICES)

    class Meta:
        model = ForOrgans
        fields = '__all__'


class SponsoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsore
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'