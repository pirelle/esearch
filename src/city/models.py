from django.db import models
from django.db.models import Model
from django.forms import CharField


# Create your models here.
class Organization(Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    type = models.IntegerField()
    rating = models.IntegerField()
    lat = models.DecimalField(max_digits=20, decimal_places=15)
    lon = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return self.title


class Tag(Model):
    title = models.CharField(max_length=255)
    organization = models.ManyToManyField(
        Organization,
        through="OrganizationTag",
    )

    def __str__(self):
        return self.title


class OrganizationTag(Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = "city_organization_tag"

    def __str__(self):
        return self.organization


class OrganizationWorkSchedule(Model):
    day_of_week = models.IntegerField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    start = models.IntegerField()
    finish = models.IntegerField()

    class Meta:
        db_table = "city_organization_work_schedule"

    def __str__(self):
        return str(self.organization)
