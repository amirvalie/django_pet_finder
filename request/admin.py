from django.contrib import admin
from .models import (
    AdopterRequest,
    AdopterRequestStatus,
)
# Register your models here.

class AdopterRequestAdmin(admin.ModelAdmin):
    pass

class AdopterRequestStatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(AdopterRequest,AdopterRequestAdmin)
admin.site.register(AdopterRequestStatus,AdopterRequestStatusAdmin)

