from django.contrib import admin
from .models import(
    PetLocation,
    Breed,
    Color,
    Pet,
    PetPicture,
    PetHealth,
    PetPersonality,
    AdditionalField,
)

admin.site.register(PetLocation)
admin.site.register(Breed)
admin.site.register(Color)
admin.site.register(Pet)
admin.site.register(PetPicture)
admin.site.register(PetHealth)
admin.site.register(PetPersonality)
admin.site.register(AdditionalField)