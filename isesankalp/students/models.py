from django.db import models

# Create your models here.
class Student(models.Model):
    #Roll_no = models.PositiveIntegerField()
    USN= models.CharField(max_length=10)
    fname= models.CharField(max_length=15)
    lname=models.CharField(max_length=15)
    email=models.EmailField(max_length=100)
    Field_of_study=models.CharField(max_length=150)
    #GPA= models.FloatField()
    Result = models.CharField(max_length=10)    
    def __str__(self):
        return f'{self.fname} {self.lname}'  
    