from django.db import models

# Create your models here.
class Album(models.Model):
	title=models.CharField(max_length=50)
	genre=models.CharField(max_length=30)
	image=models.CharField(max_length=1000)
	artist=models.CharField(max_length=50)
	def __str__(self):
		return "title: "+self.title+" artist: "+self.artist
class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	s_title=models.CharField(max_length=50)
	s_artist=models.CharField(max_length=50)
	s_duration=models.DecimalField(default=0,max_digits=12,decimal_places=4)
	s_image=models.CharField(max_length=1000)
	song_file=models.FileField(upload_to="media")
	def __str__(self):
		return "title: "+self.s_title+" artist: "+self.s_artist
	