from rest_framework import serializers
from .models import (
    AdopterRequest,
    AdopterRequestStatus,
)

class AdopterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdopterRequest
        fields='__all__'

class AdopterRequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdopterRequestStatus
        fields='__all__'

