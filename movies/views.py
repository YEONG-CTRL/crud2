import json

#from django.shortcuts import render
from django.http   import JsonResponse
from django.views import View

from movies.models import Actors, Movies, Actors_movies 
# Create your views here.
class ActorsView(View):
    def get(self,request):
        actors = Actors.objects.all()
        result_list = []    
        for actor in actors:
            try:
                results = {}
                results["first_name"] = actor.first_name
                results["last_name"]  = actor.last_name 
                movie_list = []
                for actor_movie in actor.movies_set.all():
                    movie_list.append(actor_movie.title)
                results["movie"] = movie_list
                result_list.append(results)
            except KeyError:
                for actor in actors:
                    results = {}
                    results["first_name"] = actor.first_name
                    results["last_name"]  = actor.last_name
                result_list.append(results)
        return JsonResponse({'results':result_list}, status=200)

class MoviesView(View):
    def get(self,request):
        movies = Movies.objects.all()
        result_list = []
        for movie in movies:
            results = {}
            results["title"] = movie.title
            results["running_time"] = movie.running_time
            actors = []
            actor_query = movie.actor.all()
            for i in range(len(movie.actor.all())):
                actors.append(actor_query[i].last_name)
            results["starred_actors"] = actors
            result_list.append(results)
        return JsonResponse({'results':result_list}, status=200)
	