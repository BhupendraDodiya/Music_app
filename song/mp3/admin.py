from django.contrib import admin
from mp3.models import Song

# Register your models here.
@admin.register(Song)

class SongAdmin(admin.ModelAdmin):
    list_display = ['id','song_name','singer_name','song_image','song_audio','upload_time',]