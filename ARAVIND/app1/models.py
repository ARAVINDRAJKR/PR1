from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    item=models.CharField(max_length=200)

class Aabasoft(models.Model):
    process=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    shift_time=models.CharField(max_length=100)

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()


class Pagnation(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
