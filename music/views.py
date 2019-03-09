from django.shortcuts import render
from .models import Album,Song
from django.views.generic import DetailView,ListView
# Create your views here.
class Albu(ListView):
	template_name="music/home.html"
	context_object_name="album"
	
	def get_queryset(self):
		
		a=Album.objects.all()
		
		return a

	
	
'''class Fun(ListView):
	template_name="music/home.html"
	context_object_name="album"
	def get_queryset(self):
		return Album.objects.all()'''
		
class AlbumSong(DetailView):
	model=Album
	template_name="music/detail.html"
	
class SongView(DetailView):
	model = Song
	template_name="music/song.html"
	

