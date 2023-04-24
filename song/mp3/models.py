from django.db import models

# Create your models here.
singer_choices = (
    ('Arijit Singh','Arijit Singh'),
    ('Neha Kakkar','Neha Kakkar'),
    ('Jubin Nautiyal','Jubin Nautiyal'),
)
class Song(models.Model):
    song_name = models.CharField(max_length=100)
    singer_name = models.CharField(max_length=100,choices=singer_choices)
    song_image = models.ImageField(upload_to='song_image/')
    song_audio = models.FileField(upload_to='song_audio/')
    upload_time = models.DateTimeField(auto_now_add=True)