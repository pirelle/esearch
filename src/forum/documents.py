from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from forum.models import Post


@registry.register_document
class PostDocument(Document):
    author = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "nickname": fields.TextField(),
    })
    topic = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "title": fields.TextField(),
        "section": fields.ObjectField(properties={
            "id": fields.IntegerField(),
            "title": fields.TextField(),
            "description": fields.TextField(),
            "sub_forum": fields.ObjectField(properties={
                "id": fields.IntegerField(),
                "title": fields.TextField(),
            })
        })
    })
    content = fields.TextField(
        analyzer="content",
    )

    class Index:
        name = 'forum_posts'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
            "analysis": {
                "analyzer": {
                    "content": {
                        "tokenizer": "standard",
                        "filter": [
                            "lowercase",
                            "stop",
                            "snowball",
                        ],
                        "char_filter": ["html_strip", "bb_tags"],
                    },
                },
                "char_filter": {
                    "bb_tags": {
                        "type": "pattern_replace",
                        "pattern": "\[\/?\w+\]",
                        "replacement": "",
                    }
                },
            }
        }

    class Django:
        model = Post
        fields = [
            'id',
            'created',
        ]
