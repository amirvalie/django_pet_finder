from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
from adopter.models import AdopterInformation
from pet.models import Pet
# Create your models here.
class AdopterRequest(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    adopter_information=models.ManyToManyField(
        AdopterInformation,
    )
    pet=models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

class AdopterRequestStatus(models.Model):
    adopter_request=models.ForeignKey(
        AdopterRequest,
        on_delete=models.CASCADE
    )
    STATUS=[
        ('pending','Pending'),
        ('accept','Accept'),
        ('reject','Reject'),
    ]
    staus=models.CharField(
        max_length=15,
        choices=STATUS,
        default='pending'
    )
    title=models.CharField(
        max_length=250,
    )
    body=models.TextField()


