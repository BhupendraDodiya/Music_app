from django.shortcuts import render
from rest_framework import generics
from .serializers import SongSerializer
from mp3.models import Song


class song_create_display(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class song_update_delete_get(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer