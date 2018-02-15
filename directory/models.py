from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)

class Profile(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=256)
    category = models.ManyToManyField(Category)
    offers_private_lessons = models.BooleanField(default=False)
    address = models.TextField()
    bio = models.TextField()
    website = models.URLField(max_length=256)
    phone = models.CharField(max_length=20)
    profile_img_url = models.URLField(max_length=256)
    time_created = models.DateTimeField()
    last_modified = models.DateTimeField()

class SocialField(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(max_length=256)
    url = models.URLField()
