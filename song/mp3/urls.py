from django.urls import path
from mp3 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='home'),
    path('add_song/',views.add_song,name='add'),
    path('artist/<str:name>/',views.artist,name='artist'),
    path('song/<int:uid>/',views.song.as_view(),name='song-data'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
