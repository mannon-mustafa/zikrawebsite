from django.db import models

# Create your models here.
class diary_nursary(models.Model):
    #fee_status=models.BooleanField(default='True')
    #name = models.CharField(max_length=50)
    rollno=models.IntegerField()
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
    #def __str__(self):
       # return self. name
    def __str__(self):
        return self. rollno
    def __str__(self):
        return self. grade
    def __str__(self):
        return self. english
    def __str__(self):
        return self. urdu
    def __str__(self):
        return self. sst
    def __str__(self):
        return self. math
    def __str__(self):
        return self.science
    def __str__(self):
        return self.computer
    def __str__(self):
        return self.islamiyat
    def __str__(self):
        return self.kashmiri
    #def __str__(self):
       # return self.conduct

class diary_lkg(models.Model):
    #fee_status=models.BooleanField(default='True')
    #name = models.CharField(max_length=50)
    rollno=models.IntegerField()
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
    #def __str__(self):
       # return self. name
    def __str__(self):
        return self. rollno
    def __str__(self):
        return self. grade
    def __str__(self):
        return self. english
    def __str__(self):
        return self. urdu
    def __str__(self):
        return self. sst
    def __str__(self):
        return self. math
    def __str__(self):
        return self.science
    def __str__(self):
        return self.computer
    def __str__(self):
        return self.islamiyat
    def __str__(self):
        return self.kashmiri


class diary_ukg(models.Model):
    #fee_status=models.BooleanField(default='True')
    #name = models.CharField(max_length=50)
    rollno=models.IntegerField()
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
    #def __str__(self):
       # return self. name
    def __str__(self):
        return self. rollno
    def __str__(self):
        return self. grade
    def __str__(self):
        return self. english
    def __str__(self):
        return self. urdu
    def __str__(self):
        return self. sst
    def __str__(self):
        return self. math
    def __str__(self):
        return self.science
    def __str__(self):
        return self.computer
    def __str__(self):
        return self.islamiyat
    def __str__(self):
        return self.kashmiri


class diary_first(models.Model):
    #fee_status=models.BooleanField(default='True')
    #name = models.CharField(max_length=50)
    rollno=models.IntegerField()
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
    #def __str__(self):
       # return self. name
    def __str__(self):
        return self. rollno
    def __str__(self):
        return self. grade
    def __str__(self):
        return self. english
    def __str__(self):
        return self. urdu
    def __str__(self):
        return self. sst
    def __str__(self):
        return self. math
    def __str__(self):
        return self.science
    def __str__(self):
        return self.computer
    def __str__(self):
        return self.islamiyat
    def __str__(self):
        return self.kashmiri


class diary_second(models.Model):
    #fee_status=models.BooleanField(default='True')
    #name = models.CharField(max_length=50)
    rollno=models.IntegerField()
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
    #def __str__(self):
       # return self. name
    def __str__(self):
        return self. rollno
    def __str__(self):
        return self. grade
    def __str__(self):
        return self. english
    def __str__(self):
        return self. urdu
    def __str__(self):
        return self. sst
    def __str__(self):
        return self. math
    def __str__(self):
        return self.science
    def __str__(self):
        return self.computer
    def __str__(self):
        return self.islamiyat
    def __str__(self):
        return self.kashmiri


class diary_third(models.Model):
    #fee_status=models.BooleanField(default='True')
    #name = models.CharField(max_length=50)
    rollno=models.IntegerField()
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
    #def __str__(self):
       # return self. name
    def __str__(self):
        return self. rollno
    def __str__(self):
        return self. grade
    def __str__(self):
        return self. english
    def __str__(self):
        return self. urdu
    def __str__(self):
        return self. sst
    def __str__(self):
        return self. math
    def __str__(self):
        return self.science
    def __str__(self):
        return self.computer
    def __str__(self):
        return self.islamiyat
    def __str__(self):
        return self.kashmiri


class diary_fourth(models.Model):
    #fee_status=models.BooleanField(default='True')
    #name = models.CharField(max_length=50)
    rollno=models.IntegerField()
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
    #def __str__(self):
       # return self. name
    def __str__(self):
        return self. rollno
    def __str__(self):
        return self. grade
    def __str__(self):
        return self. english
    def __str__(self):
        return self. urdu
    def __str__(self):
        return self. sst
    def __str__(self):
        return self. math
    def __str__(self):
        return self.science
    def __str__(self):
        return self.computer
    def __str__(self):
        return self.islamiyat
    def __str__(self):
        return self.kashmiri



class diary_fees(models.Model):
    grade= models.CharField(max_length=50)
    rollno=models.IntegerField()
    fee_status=models.BooleanField(default='True')


    def __str__(self):
        return self.grade
    def __int__(self):
        return self.rollno


