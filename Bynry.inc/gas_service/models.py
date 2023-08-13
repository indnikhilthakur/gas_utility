from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    )
    REQUEST_TYPE_CHOICES = (
        ('Gas Booking', 'Gas Booking'),
        ('New Connection', 'New Connection'),
        ('Issues in Connection', 'Issues in Connection'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100, choices=REQUEST_TYPE_CHOICES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

class CustomerSupportInteraction(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    )
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)