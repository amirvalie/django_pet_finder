from django.shortcuts import render
from rest_framework import mixins, views
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet,ViewSet
from pet.permissions import IsSuperUserOrAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .permissions import IsSuperUserOrOwner
from .serializers import (
    AdopterProfileSerializer,
    AdopterInformationSerializer,
    InputSerializer,
    MCSSInputOptionSerializer,
    MCMSInputOptionSerializer,
    UFInputOptionSerializer,
    NAInputOptionSerializer,
    STVCInputOptionSerializer,
)
from .models import (
    AdopterProfile,
    AdopterInformation,
    Input,
    MCSSInputOption,
    MCMSInputOption,
    UFInputOption,
    NAInputOption,
    STVCInputOption,
)
# Create your views here.

class AdopterProfileViewset(ModelViewSet):
    permission_classes =[IsSuperUserOrOwner]
    queryset=AdopterProfile.objects.all()
    serializer_class=AdopterProfileSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AdopterInformationViewSet(ModelViewSet):
    permission_classes =[IsSuperUserOrAuthorOrReadOnly]
    queryset=AdopterInformation.objects.all()
    serializer_class=AdopterInformationSerializer

class InputViewSet(ModelViewSet):
    permission_classes =[IsSuperUserOrAuthorOrReadOnly]
    queryset=Input.objects.all()
    serializer_class=InputSerializer

class MCSSInputOptionViewSet(ModelViewSet):
    permission_classes =[IsSuperUserOrAuthorOrReadOnly]
    queryset=MCSSInputOption.objects.all()
    serializer_class=MCSSInputOptionSerializer

class MCMSInputOptionViewSet(ModelViewSet):
    permission_classes =[IsSuperUserOrAuthorOrReadOnly]
    queryset=MCMSInputOption.objects.all()
    serializer_class=MCMSInputOptionSerializer

class UFInputOptionViewSet(ModelViewSet):
    permission_classes =[IsSuperUserOrAuthorOrReadOnly]
    queryset=UFInputOption.objects.all()
    serializer_class=UFInputOptionSerializer

class NAInputOptionViewSet(ModelViewSet):
    permission_classes =[IsSuperUserOrAuthorOrReadOnly]
    queryset=NAInputOption.objects.all()
    serializer_class=NAInputOptionSerializer


class STVCInputOptionViewSet(ModelViewSet):
    permission_classes =[IsSuperUserOrAuthorOrReadOnly]
    queryset=STVCInputOption.objects.all()
    serializer_class=STVCInputOptionSerializer