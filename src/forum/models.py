from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


# Create your models here.
class SubForum(Model):
    title = models.CharField(max_length=255)

    class Meta:
        db_table = 'forum_sub_forum'

    def __str__(self):
        return self.title


class Section(Model):
    sub_forum = models.ForeignKey(SubForum, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Topic(Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Account(Model):
    nickname = models.CharField(max_length=255)

    class Meta:
        db_table = "user_account"

    def __str__(self):
        return self.nickname


class Post(Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.topic)
