from django.db import models

# Create your models here.



class marquee(models.Model):
    news_item = models.CharField(max_length=500)


class performance(models.Model):
   
    name = models.CharField(max_length=50)
    rollno=models.IntegerField()
    grade = models.CharField(max_length=50)
    english = models.CharField(max_length=50)
    urdu = models.CharField(max_length=50)
    sst = models.CharField(max_length=50)
    math = models.CharField(max_length=50)
    science = models.CharField(max_length=50)
    computer = models.CharField(max_length=50)
    islamiyat = models.CharField(max_length=50)
    kashmiri = models.CharField(max_length=50)
    conduct = models.CharField(max_length=300)


class programs(models.Model):
    caption=models.CharField(max_length=600)
    video=models.FileField(upload_to="video/%y",null=True)
    


class principal_message(models.Model):
      video=models.FileField(upload_to="video/%y",null=True)
      caption=models.CharField(max_length=600)

class diary_nursary(models.Model):
   
    #name = models.CharField(max_length=50)
    #rollno=models.IntegerField()
    grade = models.CharField(max_length=50)
    english = models.CharField(max_length=100)
    urdu = models.CharField(max_length=100)
    sst = models.CharField(max_length=100)
    math = models.CharField(max_length=100)
    science = models.CharField(max_length=100)
    computer = models.CharField(max_length=100)
    islamiyat = models.CharField(max_length=100)
    kashmiri = models.CharField(max_length=100)
    #conduct = models.CharField(max_length=300)


class diary_lkg(models.Model):
   
    #name = models.CharField(max_length=50)
    #rollno=models.IntegerField()
    grade = models.CharField(max_length=50)
    english = models.CharField(max_length=100)
    urdu = models.CharField(max_length=100)
    sst = models.CharField(max_length=100)
    math = models.CharField(max_length=100)
    science = models.CharField(max_length=100)
    computer = models.CharField(max_length=100)
    islamiyat = models.CharField(max_length=100)
    kashmiri = models.CharField(max_length=100)

class diary_ukg(models.Model):
    #name = models.CharField(max_length=50)
    #rollno=models.IntegerField()
    grade = models.CharField(max_length=50)
    english = models.CharField(max_length=100)
    urdu = models.CharField(max_length=100)
    sst = models.CharField(max_length=100)
    math = models.CharField(max_length=100)
    science = models.CharField(max_length=100)
    computer = models.CharField(max_length=100)
    islamiyat = models.CharField(max_length=100)
    kashmiri = models.CharField(max_length=100)

class diary_first(models.Model):   
    #name = models.CharField(max_length=50)
    #rollno=models.IntegerField()
    grade = models.CharField(max_length=50)
    english = models.CharField(max_length=100)
    urdu = models.CharField(max_length=100)
    sst = models.CharField(max_length=100)
    math = models.CharField(max_length=100)
    science = models.CharField(max_length=100)
    computer = models.CharField(max_length=100)
    islamiyat = models.CharField(max_length=100)
    kashmiri = models.CharField(max_length=100)

class diary_second(models.Model):   
    #name = models.CharField(max_length=50)
    #rollno=models.IntegerField()
    grade = models.CharField(max_length=50)
    english = models.CharField(max_length=100)
    urdu = models.CharField(max_length=100)
    sst = models.CharField(max_length=100)
    math = models.CharField(max_length=100)
    science = models.CharField(max_length=100)
    computer = models.CharField(max_length=100)
    islamiyat = models.CharField(max_length=100)
    kashmiri = models.CharField(max_length=100)

class diary_third(models.Model):   
    #name = models.CharField(max_length=50)
    #rollno=models.IntegerField()
    grade = models.CharField(max_length=50)
    english = models.CharField(max_length=100)
    urdu = models.CharField(max_length=100)
    sst = models.CharField(max_length=100)
    math = models.CharField(max_length=100)
    science = models.CharField(max_length=100)
    computer = models.CharField(max_length=100)
    islamiyat = models.CharField(max_length=100)
    kashmiri = models.CharField(max_length=100)

class diary_fourth(models.Model):   
    #name = models.CharField(max_length=50)
    
    grade = models.CharField(max_length=50)
    english = models.CharField(max_length=100)
    urdu = models.CharField(max_length=100)
    sst = models.CharField(max_length=100)
    math = models.CharField(max_length=100)
    science = models.CharField(max_length=100)
    computer = models.CharField(max_length=100)
    islamiyat = models.CharField(max_length=100)
    kashmiri = models.CharField(max_length=100)


class diary_fees(models.Model):
    grade = models.CharField(max_length=50)
    rollno=models.IntegerField()
    fee_status=models.BooleanField(default='True')
