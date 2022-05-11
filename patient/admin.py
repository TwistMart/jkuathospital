from django.contrib import admin
from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display=['name','phone','email', 'age', 'gender', 'created_at']
    search_fields=['name', 'phone', 'email', 'age']
    list_filter=['gender']
    list_per_page=5


# Register your models here.
admin.site.register(Patient, PatientAdmin)
