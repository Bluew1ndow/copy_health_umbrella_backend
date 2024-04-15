from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    clinics_table
)



class ClinicsResource(resources.ModelResource):
    class Meta:
        model = clinics_table
        fields = ('id', 'name', 'show', 'text', 'summary', 'image_link')

