from django.db import models

# Create your models here.
class marquee(models.Model):
    news_item = models.CharField(max_length=500)
    
    def __str__(self):
        return self. news_item

class notice_board(models.Model):
    heading=models.CharField(max_length=50)
    notice = models.CharField(max_length=500)


    def __str__(self):
        return self. heading
    def __str__(self):
        return self. notice

class image_slider(models.Model):
    image=models.ImageField(upload_to='uploads/')

    def __img__(self):
        return self. image   