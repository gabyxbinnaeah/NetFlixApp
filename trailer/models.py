from django.db import models

# Create your models here.
class Movie(models.Model):
    
    title= models.CharField(max_length=50, blank = True, null = True)
    overview = models.CharField(max_length=1000, blank = True, null = True)
    poster_path = models.CharField(max_length=4000, blank = True, null = True)
    vote_average = models.CharField(max_length=20, blank = True, null = True)
    vote_count = models.CharField(max_length=50,blank = True, null = True)
   

    def __str__(self):
        return self.title 

    def save_images(self):
        self.save()
