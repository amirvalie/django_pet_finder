from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    AdopterRequestViewSet,
    AdopterRequestStatusViewSet,
)
router=DefaultRouter()

router.register('adopter_request',AdopterRequestViewSet)
router.register('adopter_request_status',AdopterRequestStatusViewSet)

urlpatterns=[
    path('',include(router.urls)),
]