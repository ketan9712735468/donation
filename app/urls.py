from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'slider', views.SliderViewSet)
router.register(r'our-volunteers', views.OurVolunteersViewSet)


urlpatterns = [
    path('become-volunteer/',views.BecomeVolunteerView.as_view(),name='become-volunteer'),
    path('', include(router.urls)),
]