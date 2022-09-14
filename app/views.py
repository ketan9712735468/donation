from app.paginations import CustomPagination
from rest_framework.response import Response
from app.models import Blog, Contact, Donor, ForOrgans, Gallery, OurVolunteers, Slider, Sponsore
from app.serializers import BecomeVolunteerSerializer, BlogSerializer, ContactSerializer, DonorSerializer, ForOrgansSerializer, GallerySerializer, OurVolunteersSerializer, SliderSerializer, SponsoreSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework import filters


class BecomeVolunteerView(APIView):
    def post(self, request, format=None):
        serializer = BecomeVolunteerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class OurVolunteersViewSet(viewsets.ModelViewSet):
    queryset = OurVolunteers.objects.all()
    serializer_class = OurVolunteersSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email']

    # def list(self, request, *args, **kwargs):
    #     # limit = request.GET.get('limit',None)
    #     # page = request.GET.get('page', None)
    #     # if limit and page:
    #     #     data = int(limit)*int(page)
    #     #     data = data - int(limit)
    #     #     print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',data)
    #     #     total = self.queryset.count()
    #     #     contact = Contact.objects.all()[data:]
    #     #     print("🚀 ~ file: views.py ~ line 39 ~ contact", contact)
    #     # else:
    #     contact = Contact.objects.all()
    #     serializer = self.get_serializer(contact, many=True)
    #     return Response(serializer.data)

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


class SponsoreViewSet(viewsets.ModelViewSet):
    queryset = Sponsore.objects.all()
    serializer_class = SponsoreSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer