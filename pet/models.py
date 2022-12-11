from django.db import models

# Create your models here.
from django.db.models.signals import (
    pre_save
)
from django.dispatch import receiver

GENDER_CHOISES=[
    ('F','femail'),
    ('M','mail'),
]
TYPE_CHOISES=[
    ('cat','cat'),
    ('dog','dog'),
]

class PetLocation(models.Model):
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.TextField()
    zip_code=models.CharField(max_length=10)
    person=models.ForeignKey(User, on_delete=models.PROTECT)

class Pet(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    animal_type=models.CharField(max_length=3,choices=TYPE_CHOISES)
    gender = models.CharField(max_length=1,choices=GENDER_CHOISES)
    age = models.IntegerField()
    breed=models.CharField(max_length=50)
    abount=models.TextField()
    location=models.ForeignKey(PetLocation, on_delete=models.PROTECT)
    created=models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PetPicture(models.Model):
    pet=models.ForeignKey(Pet, on_delete=models.CASCADE)
    pciture=models.ImageField()



