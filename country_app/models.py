from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

class Country(models.Model):
    """
    Model to store country information fetched from REST Countries API
    """
    cca2 = models.CharField(max_length=2, primary_key=True)
    name_common = models.CharField(max_length=255)
    name_official = models.CharField(max_length=255)
    capital = models.JSONField(null=True, blank=True)  # Using JSONField as capital can be a list
    region = models.CharField(max_length=100, null=True, blank=True)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    population = models.BigIntegerField(default=0)
    languages = models.JSONField(null=True, blank=True)
    timezones = models.JSONField(null=True, blank=True)
    flags = models.JSONField(null=True, blank=True)
    latlng = models.JSONField(null=True, blank=True)  # Latitude and longitude as a list
    borders = models.JSONField(null=True, blank=True)
    currencies = models.JSONField(null=True, blank=True)
    continents = models.JSONField(null=True, blank=True)
    
    # Additional fields to store all JSON data for future use
    raw_data = models.JSONField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name_common']
    
    def __str__(self):
        return self.name_common