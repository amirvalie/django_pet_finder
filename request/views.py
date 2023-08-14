from django.shortcuts import render
from rest_framework import viewsets
from pet.permissions import IsSuperUserOrAuthorOrReadOnly
from .serializers import (
    AdopterRequestSerializer,
    AdopterRequestStatusSerializer,
)
from .models import (
    AdopterRequest,
    AdopterRequestStatus,
)
# Create your views here.


class AdopterRequestViewSet(viewsets.ModelViewSet):
    serializer_class=AdopterRequestSerializer
    queryset=AdopterRequest.objects.all()
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]

class AdopterRequestStatusViewSet(viewsets.ModelViewSet):
    serializer_class=AdopterRequestStatusSerializer
    queryset=AdopterRequestStatus.objects.all()
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]

