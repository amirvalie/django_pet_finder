from django.contrib import admin
from .models import (
    # AdapterProfile,
    AdapterInformation,
    Input,
    MCSSInputOption,
    UFInputOption,
    NAInputOption,
    STVCInputOption,
)

# admin.site.register(AdapterProfile)
admin.site.register(AdapterInformation)
admin.site.register(Input)
admin.site.register(MCSSInputOption)
admin.site.register(UFInputOption)
admin.site.register(NAInputOption)
admin.site.register(STVCInputOption)