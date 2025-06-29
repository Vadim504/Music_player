from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.artists.models import Artist

class Track(models.Model):
    """Track model for music player"""
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tracks')
    album = models.CharField(max_length=200, blank=True)
    duration = models.DurationField()  # Duration in seconds
    file = models.FileField(upload_to='tracks/')
    cover_art = models.ImageField(upload_to='covers/', null=True, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    release_date = models.DateField(null=True, blank=True)
    lyrics = models.TextField(blank=True)
    play_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']
        unique_together = ['title', 'artist']
    
    def __str__(self):
        return f"{self.title} - {self.artist.name}"
