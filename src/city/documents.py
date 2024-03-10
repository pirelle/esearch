from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from city.models import Organization


organization_schedule_props = {
    "start": fields.IntegerField(),
    "finish": fields.IntegerField(),
}

@registry.register_document
class OrganizationDocument(Document):
    location = fields.GeoPointField()
    tags = fields.TextField(
        attr='tags_indexing',
        multi=True,
        priority=2,
    )
    d1 = fields.ObjectField(properties=organization_schedule_props)
    d2 = fields.ObjectField(properties=organization_schedule_props)
    d3 = fields.ObjectField(properties=organization_schedule_props)
    d4 = fields.ObjectField(properties=organization_schedule_props)
    d5 = fields.ObjectField(properties=organization_schedule_props)
    d6 = fields.ObjectField(properties=organization_schedule_props)
    d7 = fields.ObjectField(properties=organization_schedule_props)

    class Index:
        name = 'city_organizations'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Organization
        queryset_pagination = 5000
        fields = [
            'id',
            'title',
            'description',
            'type',
            'rating',
        ]

    def prepare(self, instance):
        data = super().prepare(instance)
        for work_schedule in instance.organizationworkschedule_set.all():
            data[f"d{work_schedule.day_of_week}"] = {
                "start": work_schedule.start,
                "finish": work_schedule.finish,
            }
        return data

    def get_queryset(self):
        return super().get_queryset().prefetch_related('organizationworkschedule_set')
