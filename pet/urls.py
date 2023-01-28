
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
        PetViewSet,
        PetPersonalityViewSet,
        PetHealthViewSet,
        PetLocationViewSet,
        PetPictureViewSet,
        ColorViewSet,
        BreedViewSet,
        AdditionalFieldViewSet,
        PetLocationViewSet,
        CategoryViewSet,
    )

router = DefaultRouter()

router.register('pet_info',PetViewSet)
router.register('pet_personality',PetPersonalityViewSet)
router.register('pet_health',PetHealthViewSet)
router.register('pet_location',PetLocationViewSet)
router.register('pet_picture',PetPictureViewSet)
router.register('color',ColorViewSet)
router.register('breed',BreedViewSet)
router.register('add_field',AdditionalFieldViewSet)
router.register('pet_location',PetLocationViewSet)
router.register('category',CategoryViewSet)

urlpatterns = [
    path('', include((router.urls))),
]


