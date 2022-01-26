from django.contrib import admin
from .models import Patient

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'ref', 'ap', 'apl', 'lat', 'latl', 'date_of_update')
    #ordering = ['-date_of_update']
