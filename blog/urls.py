from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    BlogCategoryViewSet,
    ArticleViewSet,
)
router=DefaultRouter()

router.register('blog_category',BlogCategoryViewSet)
router.register('article',ArticleViewSet)

urlpatterns=[
    path('',include(router.urls)),
]