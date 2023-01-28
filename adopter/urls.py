from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    AdopterProfileViewset,
    AdopterInformationViewSet,
    InputViewSet,
    MCSSInputOptionViewSet,
    MCMSInputOptionViewSet,
    UFInputOptionViewSet,
    NAInputOptionViewSet,
    STVCInputOptionViewSet,
)

router=DefaultRouter()

router.register('adopter_profile',AdopterProfileViewset)
router.register('adopter_info',AdopterInformationViewSet)
router.register('input',InputViewSet)
router.register('mcss_input_option',MCSSInputOptionViewSet)
router.register('mcms_input_option',MCMSInputOptionViewSet)
router.register('ufi_input_option',UFInputOptionViewSet)
router.register('na_input_option',NAInputOptionViewSet)
router.register('stv_input_option',STVCInputOptionViewSet)

urlpatterns=[
    path('',include(router.urls)),
]

