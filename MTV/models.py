from tkinter import CASCADE
from django.db import models

#Create your models here.

class Manager(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=40, blank=False, null=False)
  phone = models.CharField(max_length=40, blank=False, null=False)
  
  def __str__(self):
    return self.name

class Car(models.Model):
  name = models.CharField(max_length=30)
  age = models.CharField(max_length=500)
  model = models.CharField(max_length=80, default="")
  kilo = models.IntegerField()
  price = models.IntegerField()
  date = models.DateTimeField(auto_now_add=True)
  owner = models.CharField(max_length=30)
  quality_score = models.IntegerField(default=100)
  price_score = models.IntegerField(default=100)
  img = models.CharField(max_length=30,default="")
  manager = models.ForeignKey(Manager,on_delete=models.DO_NOTHING,default="0")
  
  def __str__(self):
    return self.name

class OptionA(models.Model):
  Car = models.ForeignKey(Car,on_delete=models.CASCADE)
  opt1 = models.BooleanField(default=False)
  opt2 = models.BooleanField(default=False)
  opt3 = models.BooleanField(default=False)
  opt4 = models.BooleanField(default=False)
  opt5 = models.BooleanField(default=False)
  opt6 = models.BooleanField(default=False)
  opt7 = models.BooleanField(default=False)
  opt8 = models.BooleanField(default=False)
  opt9 = models.BooleanField(default=False)
  opt10 = models.BooleanField(default=False)
  
  
    
class OptionB(models.Model):
  Car = models.ForeignKey(Car,on_delete=models.CASCADE)
  opt1 = models.BooleanField(default=False)
  opt2 = models.BooleanField(default=False)
  opt3 = models.BooleanField(default=False)
  opt4 = models.BooleanField(default=False)
  opt5 = models.BooleanField(default=False)
  opt6 = models.BooleanField(default=False)
  opt7 = models.BooleanField(default=False)
  opt8 = models.BooleanField(default=False)
  opt9 = models.BooleanField(default=False)
  opt10 = models.BooleanField(default=False)
  opt11 = models.BooleanField(default=False) 
  opt12 = models.BooleanField(default=False) 

class OptionC(models.Model):
  Car = models.ForeignKey(Car,on_delete=models.CASCADE)
  opt1 = models.BooleanField(default=False)
  opt2 = models.BooleanField(default=False)
  opt3 = models.BooleanField(default=False)
  opt4 = models.BooleanField(default=False)
  opt5 = models.BooleanField(default=False)
  opt6 = models.BooleanField(default=False)
  opt7 = models.BooleanField(default=False)
  opt8 = models.BooleanField(default=False)
  opt9 = models.BooleanField(default=False)
  opt10 = models.BooleanField(default=False)
  
class OptionD(models.Model):
  Car = models.ForeignKey(Car,on_delete=models.CASCADE)
  opt1 = models.BooleanField(default=False)
  opt2 = models.BooleanField(default=False)
  opt3 = models.BooleanField(default=False)
  opt4 = models.BooleanField(default=False)
  opt5 = models.BooleanField(default=False)
  opt6 = models.BooleanField(default=False)
  opt7 = models.BooleanField(default=False)
  opt8 = models.BooleanField(default=False)
  opt9 = models.BooleanField(default=False)
  opt10 = models.BooleanField(default=False)