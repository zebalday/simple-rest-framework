from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Director(models.Model):


    name = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=False, blank=True)
    detail_url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return (f"{self.name}, {self.country}")


@receiver(pre_save, sender=Director)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

@receiver(post_save, sender=Director)
def set_detail_url(sender, instance, **kwargs):
    if not instance.detail_url:
        instance.detail_url = f"http://127.0.0.1:8000/api/viewsets/directors/{instance.id}"
        instance.save()


class Movie(models.Model):


    name = models.CharField(max_length=120, null=False, blank=False)
    release_date = models.DateField(null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=False, blank=True)
    detail_url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return (f"{self.name}, {self.director.name}")


@receiver(pre_save, sender=Movie)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

@receiver(post_save, sender=Movie)
def set_detail_url(sender, instance, **kwargs):
    if not instance.detail_url:
        instance.detail_url = f"http://127.0.0.1:8000/api/viewsets/movies/{instance.id}"
        instance.save()