from django.contrib import admin
from .models import (
    AdopterProfile,
    AdopterInformation,
    Input,
    MCSSInputOption,
    UFInputOption,
    NAInputOption,
    STVCInputOption,
)

class MCSSInputModelAmdin(admin.TabularInline):
    model=MCSSInputOption

class UFInputAmdin(admin.TabularInline):
    model=UFInputOption

class NAInputModelAmdin(admin.TabularInline):
    model=NAInputOption

class STVCInputModelAmdin(admin.TabularInline):
    model=STVCInputOption


class InputModelAdmin(admin.ModelAdmin):
    inlines=[
        MCSSInputModelAmdin,
        STVCInputModelAmdin,
        NAInputModelAmdin,
        UFInputAmdin,
    ]
    list_display=[
        'title',
        'description',
        'input_type',
    ]

admin.site.register(AdopterInformation)
admin.site.register(Input,InputModelAdmin)
admin.site.register(AdopterProfile)
