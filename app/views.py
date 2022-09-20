from app.paginations import CustomPagination
from rest_framework.response import Response
from app.models import BecomeVolunteer, Blog, Contact, Donor, ForOrgans, Gallery, OurVolunteers, Slider, Sponsore
from app.serializers import BecomeVolunteerSerializer, BlogSerializer, ContactSerializer, DonorSerializer, ForOrgansSerializer, GallerySerializer, OurVolunteersSerializer, SliderSerializer, SponsoreSerializer
from rest_framework import viewsets, status
from rest_framework import filters


class BecomeVolunteerView(viewsets.ModelViewSet):
    queryset = BecomeVolunteer.objects.all()
    serializer_class = BecomeVolunteerSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email', 'number']


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class OurVolunteersViewSet(viewsets.ModelViewSet):
    queryset = OurVolunteers.objects.all()
    serializer_class = OurVolunteersSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # send_email()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email']


class ForOrgansViewSet(viewsets.ModelViewSet):
    queryset = ForOrgans.objects.all()
    serializer_class = ForOrgansSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'middle_name', 'last_name', 'city', 'email']


class SponsoreViewSet(viewsets.ModelViewSet):
    queryset = Sponsore.objects.all()
    serializer_class = SponsoreSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['heading']


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
