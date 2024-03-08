from django.contrib import admin

from city.models import OrganizationWorkSchedule, OrganizationTag, Tag, Organization

# Register your models here.
admin.site.register(Organization)
admin.site.register(Tag)
admin.site.register(OrganizationTag)
admin.site.register(OrganizationWorkSchedule)
