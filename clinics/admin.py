from django.contrib import admin
from .models import clinics_table
from .resources import *
from import_export.admin import ImportExportModelAdmin

class ClinicsAdmin(ImportExportModelAdmin):
    resource_class = ClinicsResource
    list_filter = ("show",)
    search_fields = ("name",)

admin.site.register(clinics_table, ClinicsAdmin)
