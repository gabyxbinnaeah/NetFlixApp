from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.get_movies, name="get_movies"),
    path('youtube/<id>',views.youtube,name = 'youtube'),
]