from django.contrib import admin
from .models import User, Doctor, Patient, Appointment, Prescription, Invoice

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth')


admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Invoice)
