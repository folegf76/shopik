from django.db import models

# Create your models here.


class OurPluses(models.Model):
    name = models.CharField(max_length=100, unique=True)
    position = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='ourpluses/%Y/%m/%d')
    description = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.name}  {self.position}'


class AboutGallery(models.Model):
    name = models.CharField(max_length=100, unique=True)
    position = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='gallery/%Y/%m/%d')
    description = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.name}  {self.position}'


class WhatCan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    position = models.PositiveSmallIntegerField()
    description = models.TextField(max_length=200)
    description1 = models.TextField(max_length=200, blank=True)
    description2 = models.TextField(max_length=200, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.name}  {self.position}'


class CustomersSays(models.Model):
    name = models.CharField(max_length=100)
    professional = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='gallery/%Y/%m/%d')
    description = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.name}  {self.position}'
