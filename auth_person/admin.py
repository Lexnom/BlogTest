from django.contrib import admin
from auth_person.models import User, Subscriber, Post_news
# Register your models here.
admin.site.register(User)
admin.site.register(Subscriber)
admin.site.register(Post_news)