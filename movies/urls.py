from django.urls import path

from movies.views import ActorsView, MoviesView

urlpatterns = [
    path('/movie', MoviesView.as_view()),
    path('/actor', ActorsView.as_view())
]