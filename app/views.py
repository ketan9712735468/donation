from rest_framework.response import Response
from app.models import Contact, Donor, ForOrgans, OurVolunteers, Slider
from app.serializers import BecomeVolunteerSerializer, ContactSerializer, DonorSerializer, ForOrgansSerializer, OurVolunteersSerializer, SliderSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # send_email()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer


class ForOrgansViewSet(viewsets.ModelViewSet):
    queryset = ForOrgans.objects.all()
    serializer_class = ForOrgansSerializer