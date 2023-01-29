from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import (
    PetSerializer,
    PetPersonalitySerializer,
    PetHealthSerializer,
    PetPictureSerializer,
    BreedSerializer,
    AdditionalFieldSerializer,
    ColorSerializer,
    PetLocationSerializer,
    CategorySerializer,
)
from .models import (
    Pet,
    PetPersonality,
    PetHealth,
    PetLocation,
    PetPicture,
    Color,
    Breed,
    AdditionalField,
    PetCategory,
)
from .permissions import IsSuperUserOrAuthorOrReadOnly
from rest_framework.response import Response

class PetViewSet(viewsets.ModelViewSet):
    permission_classes =[IsSuperUserOrAuthorOrReadOnly]
    queryset=Pet.objects.all()
    serializer_class=PetSerializer

class PetPersonalityViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=PetPersonality.objects.all()
    serializer_class=PetPersonalitySerializer

class PetHealthViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=PetHealth.objects.all()
    serializer_class=PetHealthSerializer

class PetLocationViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=PetLocation.objects.all()
    serializer_class=PetPictureSerializer

class PetPictureViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=PetPicture.objects.all()
    serializer_class=PetPictureSerializer

class ColorViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=Color.objects.all()
    serializer_class=ColorSerializer
    
class BreedViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=Breed.objects.all()
    serializer_class=BreedSerializer
    
class AdditionalFieldViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=AdditionalField.objects.all()
    serializer_class=AdditionalFieldSerializer

class PetLocationViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=PetLocation.objects.all()
    serializer_class=PetLocationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=PetCategory.objects.all()
    serializer_class=CategorySerializer