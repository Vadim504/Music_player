from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.user.models import User
from apps.tracks.models import Track

class Playlist(models.Model):
    """Playlist model for music player"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    tracks = models.ManyToManyField(Track, through='PlaylistTrack', related_name='playlists')
    cover_image = models.ImageField(upload_to='playlist_covers/', null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['name', 'owner']
    
    def __str__(self):
        return f"{self.name} by {self.owner.username}"

class PlaylistTrack(models.Model):
    """Intermediate model for playlist-track relationship with order"""
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
        unique_together = ['playlist', 'track', 'order']
    
    def __str__(self):
        return f"{self.track.title} in {self.playlist.name} (order: {self.order})"
