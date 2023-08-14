from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import(
    ArticleSerializer,
    BlogCategorySerializer,
)
from .models import (
    BlogCategory,
    Article,
)
from pet.permissions import IsSuperUserOrAuthorOrReadOnly

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=Article.objects.publish()
    serializer_class=ArticleSerializer

class BlogCategoryViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSuperUserOrAuthorOrReadOnly]
    queryset=BlogCategory.objects.all()
    serializer_class=BlogCategorySerializer

