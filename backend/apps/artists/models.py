from django.db import models
from django.utils.translation import gettext_lazy as _

class Artist(models.Model):
    """Artist model for music player"""
    name = models.CharField(max_length=200, unique=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='artists/', null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    genres = models.JSONField(default=list, blank=True)  # List of genres
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
