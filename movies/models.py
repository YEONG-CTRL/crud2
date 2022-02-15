from django.db import models

# Create your models here.
class Actors(models.Model):
    first_name     = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    date_of_birth = models.DateTimeField(auto_now=False, auto_now_add=False)
    class Meta:
        db_table = 'actors'

class Actors_movies(models.Model):
    actor    = models.ForeignKey('Actors', on_delete=models.CASCADE)
    movies = models.ForeignKey('Movies', on_delete=models.CASCADE)
    class Meta:
        db_table = 'actor_movies'


class Movies(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    running_time = models.IntegerField()
    actor = models.ManyToManyField(Actors, through='Actors_movies')		
    class Meta:
        db_table = 'movies'