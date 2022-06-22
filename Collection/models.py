from django.db import models
from django.db.models import CharField, ImageField, Model
from utils.models import file_path


class Owner(Model):
    username = models.SlugField(max_length=64, unique=True)
    picture = ImageField(upload_to=file_path('Collection/Owner/picture'))
    banner = ImageField(upload_to=file_path('Collection/Owner/banner'))
    wallet = CharField(max_length=42, blank=True, null=True)
    description = models.TextField()
    floor_price = CharField(max_length=64)
    ceil_price = CharField(max_length=64)
    rarible = models.URLField()
    twitter = CharField(max_length=30, blank=True, null=True, unique=True)
    twitter_id = models.BigIntegerField(null=True, blank=True)
    instagram = CharField(max_length=30, blank=True, null=True)
    tweet = models.TextField(default='', blank=True)

    def __str__(self):
        return self.username


class Asset(Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = ImageField(upload_to=file_path('Collection/Asset/image'))
    title = CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.owner.username}'s asset"


class FAQ(Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    question = CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question


class HitCount(Model):
    hits = models.PositiveBigIntegerField(default=0)

    def save(self, *args, **kwargs):
        first = HitCount.objects.first()
        if first:
            self.pk = first.pk
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        first = HitCount.objects.first()
        if first:
            if self.pk != first.pk:
                super().delete(*args, **kwargs)

    @classmethod
    def load(cls):
        first = cls.objects.first()
        if first:
            return first
        return cls.objects.create()

    def __str__(self):
        return f'hits: {self.hits}'
