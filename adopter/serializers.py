from rest_framework import serializers
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

class AdopterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdopterProfile
        exclude=['user']


class AdopterInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdopterInformation
        fields='__all__'

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model=Input
        fields='__all__'

class MCSSInputOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MCSSInputOption
        fields='__all__'

class MCMSInputOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MCMSInputOption
        fields='__all__'

class UFInputOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=UFInputOption
        fields='__all__'

class NAInputOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=NAInputOption
        fields='__all__'

class STVCInputOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=STVCInputOption
        fields='__all__'