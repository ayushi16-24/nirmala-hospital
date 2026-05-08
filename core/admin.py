from django.contrib import admin
from .models import Appointment, Treatment, Testimonial, GalleryImage, ContactMessage

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'appointment_date', 'treatment_type', 'is_confirmed', 'created_at']
    list_filter = ['is_confirmed', 'treatment_type', 'appointment_date']
    search_fields = ['full_name', 'phone', 'email']
    list_editable = ['is_confirmed']
    ordering = ['-created_at']

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'rating', 'treatment', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['rating', 'is_active']

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['category']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'subject', 'is_read', 'created_at']
    list_editable = ['is_read']
    list_filter = ['is_read']
    search_fields = ['name', 'email', 'subject']
