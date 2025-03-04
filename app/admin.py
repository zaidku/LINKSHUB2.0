from django.contrib import admin
from .models import Case

class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'dentist_name', 'created_at')  # Removed invalid fields

admin.site.register(Case, CaseAdmin)
