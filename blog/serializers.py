from rest_framework import serializers
from .models import (
    BlogCategory,
    Article,
)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        exclude=['author']

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogCategory
        fields='__all__'
        
