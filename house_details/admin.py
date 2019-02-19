from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . models import HouseDetails

# Register your models here.

@admin.register(HouseDetails)
class HouseDetailsAdmin(ImportExportModelAdmin):
    pass