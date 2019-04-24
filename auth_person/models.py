from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=120)



    def __str__(self):
        return self.login

class Subscriber(models.Model):
    login = models.CharField(max_length=120)
    sublogin = models.CharField(max_length=120)


class Post_news(models.Model):
    name_post = models.CharField(max_length=200)
    text_post = models.TextField()
    date_post = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_post
