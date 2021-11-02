from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)


class Advisor(models.Model):
    user_id = models.CharField(max_length=10, default="NA")
    advisor_id = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    photo_url = models.CharField(max_length=500)
    booking_time = models.CharField(max_length=20)
    booking_id = models.CharField(max_length=50)

