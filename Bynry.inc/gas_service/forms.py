from django import forms
from .models import ServiceRequest, CustomerSupportInteraction

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']

class CustomerSupportForm(forms.ModelForm):
    class Meta:
        model = CustomerSupportInteraction
        fields = ['response']