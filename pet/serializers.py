from rest_framework import serializers
from .models import (
    Pet,
    PetPersonality,
    PetHealth,
    PetLocation,
    PetPicture,
    Color,
    Breed,
    PetLocation,
    AdditionalField,
    PetCategory,
)
class PetSerializer(serializers.HyperlinkedModelSerializer):
    breed=serializers.HyperlinkedRelatedField(view_name='breed-detail',read_only=True)
    location=serializers.HyperlinkedRelatedField(view_name='petlocation-detail',read_only=True)
    pet_picture=serializers.HyperlinkedRelatedField(view_name='pet_picture-detail',many=True,read_only=True)
    pet_health=serializers.HyperlinkedRelatedField(view_name='pet_health-detail',many=True,read_only=True)
    personality=serializers.HyperlinkedRelatedField(view_name='petpersonality-detail',many=True,read_only=True)
    additional_field=serializers.HyperlinkedRelatedField(view_name='additional_field-detail',many=True,read_only=True)
    class Meta:
        model = Pet
        fields = [
            'name',
            'animal_type',
            'gender',
            'age',
            'breed',
            'location',
            'about',
            'created',
            'modified',
            'pet_picture',
            'pet_health',
            'personality',
            'additional_field',
        ]

class PetPersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model=PetPersonality
        fields='__all__'

class PetLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=PetLocation
        fields='__all__'


class PetHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model=PetHealth
        fields='__all__'
class PetPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model=PetPicture
        fields='__all__'

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Breed
        fields='__all__'

class AdditionalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdditionalField
        fields='__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=PetCategory
        fields='__all__'