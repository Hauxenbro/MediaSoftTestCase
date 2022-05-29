from django.db import models
from django.urls import reverse

# Create your models here.

class Shops(models.Model):
    title = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.PROTECT, null=True)
    street = models.ForeignKey('Street', on_delete=models.SET_NULL, null=True)
    house_number = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

class City(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Street(models.Model):
    title = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete = models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'