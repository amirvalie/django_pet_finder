from django.db import models

# Create your models here.


class PetLocation(models.Model):
    person=models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    state=models.CharField(
        max_length=50,
    )
    city=models.CharField(
        max_length=50,
    )
    address=models.TextField()
    zip_code=models.CharField(
        max_length=10,
    )

class Breed(models.Model):
    breed_name=models.CharField(
        max_length=100
    )

class Color(models.Model):
    color_name=models.CharField(max_length=30)


class Pet(models.Model):
    GENDER_CHOISES=[
        ('F','femail'),
        ('M','mail'),
    ]
    PET_TYPE=[
        ('cat','Cat'),
        ('dog','Dog'),
    ]
    name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    animal_type=models.CharField(
        choices=PET_TYPE,
        max_length=3,
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOISES
    )
    age = models.IntegerField()
    breed=models.ForeignKey(
        Breed,
        on_delete=models.PROTECT
    )
    location=models.ForeignKey(
        PetLocation,
        on_delete=models.PROTECT
    )
    about=models.TextField()
    created=models.DateTimeField(
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )

class PetPicture(models.Model):
    pet=models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )
    pciture=models.ImageField()

class PetHealth(models.Model):
    title=models.CharField(max_length=250)
    checked=models.BooleanField()
    pet=models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )