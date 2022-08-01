from django.contrib import admin
from app.models import BecomeVolunteer, Contact, Donor, ForOrgans, OurVolunteers, Slider


admin.site.register(BecomeVolunteer)
admin.site.register(Slider)
admin.site.register(OurVolunteers)
admin.site.register(Contact)
admin.site.register(Donor)
admin.site.register(ForOrgans)