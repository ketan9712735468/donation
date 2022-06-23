from app.models import Contact, Donor, OurVolunteers, Slider
from rest_framework.response import Response
from app.serializers import BecomeVolunteerSerializer, ContactSerializer, DonorSerializer, OurVolunteersSerializer, SliderSerializer
from rest_framework.views import APIView
from rest_framework import viewsets


class BecomeVolunteerView(APIView):
    def post(self, request, format=None):
        serializer = BecomeVolunteerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class OurVolunteersViewSet(viewsets.ModelViewSet):
    queryset = OurVolunteers.objects.all()
    serializer_class = OurVolunteersSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer