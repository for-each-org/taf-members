from django.contrib.postgres.fields import JSONField
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)

class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256) # TODO: Figure out how to make this work with Django's built in auth
    name = models.CharField(max_length=256)
    time_created = models.DateTimeField()
    last_modified = models.DateTimeField()

    ADMIN = 1
    USER = 0
    USER_TYPE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User')
    )
    user_type = models.IntegerField(
        choices=USER_TYPE_CHOICES,
        default=USER
    )

class Profile(models.Model):
    name = models.CharField(max_length=256)
    category = models.ManyToManyField(Category)
    offers_private_lessons = models.BooleanField(default=False)
    address = models.TextField()
    bio = models.TextField()
    website = models.URLField(max_length=256)
    phone = models.CharField(max_length=20)
    profile_img_url = models.URLField(max_length=256)
    social = JSONField()
    time_created = models.DateTimeField()
    last_modified = models.DateTimeField()


