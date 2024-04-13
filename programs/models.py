from django.db import models

# Create your models here.
class programs(models.Model):
    caption=models.CharField(max_length=600)
    video=models.FileField(upload_to="video/%y",null=True)
    
    def __str__(self):
        return self. caption
    def __video__(self):
        return self. video
    