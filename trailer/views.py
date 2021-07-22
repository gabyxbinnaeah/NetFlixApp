from django.shortcuts import render
import requests,json
from .models import Movie
from movie import settings
from decouple import config
import os
from googleapiclient.discovery import build

def index(request,category):
    url='https://api.themoviedb.org/3/movie/{}?api_key={}'
    api_key='f5122c8447d204dde714ca3eae6e3be7'
    formated_url=url.format(category,api_key)
    final_url=requests.get(formated_url).json()
    return final_url

def get_movies(request):
    all_movies = index(request,'popular')['results']    
    context={"all_movies":all_movies}
    return render(request,'movies/movie.html',context)

def youtube(request,id):
    youtubeapi =  config('youtubeapi')
    popular = index(request,'popular')
   
    pp = ''
    for p in popular['results']:
        if str(p['id'])==str(id):
            pp = p['title']
    youtube = build('youtube','v3',developerKey = youtubeapi)
    req = youtube.search().list(q= pp+'trailer',part = 'snippet',type= 'video').execute()
    
    return render(request,'youtube.html',{'response':req})