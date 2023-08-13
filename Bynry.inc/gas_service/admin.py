from django.contrib import admin
from .models import ServiceRequest, CustomerSupportInteraction

admin.site.register(ServiceRequest)
admin.site.register(CustomerSupportInteraction)

# @admin.register(ServiceRequest)
# class ServiceRequestadmin(admin.ModelAdmin):
#     list_display = ['id', 'email', 'phone_no', 'password', 'first_name', 'last_name', 'address']