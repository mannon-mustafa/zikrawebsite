from django.db import models

# Create your models here.


class performance(models.Model):
    fee_status=models.BooleanField(default='True')
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
    def __str__(self):
        return self. name
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
    def __str__(self):
        return self.conduct

