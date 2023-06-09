from django.urls import path
from api import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('song/',views.song_create_display.as_view()),
    path('song/<pk>/',views.song_update_delete_get.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)