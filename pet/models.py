from django.db import models

# Create your models here.


class Pet(models.Model):
    GENDER_CHOISES=[
        ('F','femail'),
        ('M','mail'),
    ]
    PET_LOCATION=[
        ('cat','Cat'),
        ('dog','Dog'),
    ]
    name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    animal_type=models.CharField(
        choices=PET_LOCATION,
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

