from django.shortcuts import render
from .models import Movie
import requests

def get_movies(request):

    popular_url='https://api.themoviedb.org/3/movie/popular?api_key=d3b72290034dd8b0a485d50b2ba0c46f'
    nowShowing_url=''
    response=requests.get(popular_url)
    data=response.json()
    movies=data['results'] 
 
    for contents in movies:
        movie_data=Movie(
            title=contents['title'],
            overview =contents['overview'],
            poster_path=contents['poster_path'],
            vote_average=contents['vote_average'],
            vote_count=contents['vote_count']
            )
        saved_data=movie_data.save()
        all_movies=Movie.objects.all()
    return render(request, 'movies/movie.html', {"all_movies":all_movies})




