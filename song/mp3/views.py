from django.shortcuts import render
from django.views import View
from .models import Song
# Create your views here.

def index(request):
    data = Song.objects.all()
    return render(request,'index.html',{'data':data})

class song(View):
    def get(self,request,uid):
        data = Song.objects.get(id=uid)
        return render(request,'song.html',{'i':data})

def artist(request,name):
    singer = Song.objects.filter(singer_name=name)
    print(singer)
    return render(request,'artist.html',{'singer':singer})


    