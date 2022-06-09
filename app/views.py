from app.models import OurVolunteers, Slider
from rest_framework.response import Response
from app.serializers import BecomeVolunteerSerializer, OurVolunteersSerializer, SliderSerializer
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
