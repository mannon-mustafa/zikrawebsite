from django.db import models

# Create your models here.
class principal_message(models.Model):
      video=models.FileField(upload_to="video/%y",null=True)
      caption=models.CharField(max_length=600)


      def __str__(self):
           return self. caption
      def __video__(self):
           return self. video