from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'slider', views.SliderViewSet)
router.register(r'our-volunteers', views.OurVolunteersViewSet) #
router.register(r'contact-us', views.ContactViewSet) #
router.register(r'make-donation', views.DonorViewSet) #
router.register(r'for-organs', views.ForOrgansViewSet)
router.register(r'sponsore', views.SponsoreViewSet)
router.register(r'blog', views.BlogViewSet) #
router.register(r'gallery', views.GalleryViewSet)


urlpatterns = [
    path('become-volunteer/', views.BecomeVolunteerView.as_view(),
         name='become-volunteer'),
    path('', include(router.urls)),
]
