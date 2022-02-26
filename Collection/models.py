from django.db import models
from django.db.models import Model, ImageField, CharField

# utils
from utils.models import file_path


class Owner(Model):
    username = models.SlugField(max_length=64, unique=True)
    picture = ImageField(upload_to=file_path('Collection/Owner/picture'))
    twitter = CharField(max_length=30, blank=True, null=True, unique=True)
    twitter_id = models.BigIntegerField(null=True, blank=True)
    wallet = CharField(max_length=42, blank=True, null=True)
    description = models.TextField()
    floor_price = CharField(max_length=64)
    ceil_price = CharField(max_length=64)

    def __str__(self):
        return self.username


class Asset(Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = ImageField(upload_to=file_path('Collection/Asset/image'))
    description = models.TextField()

    def __str__(self):
        return f"{self.owner.username}'s asset"