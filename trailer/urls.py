from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$',views.get_movies, name="get_movies"),
    # url(r'movies/<int:id>/',views.movie_details, name ="movie_detail"),
]