from django.contrib import admin

from forum.models import Account, Post, Topic, Section, SubForum

# Register your models here.
# create admin pages for all models
admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Section)
admin.site.register(SubForum)
