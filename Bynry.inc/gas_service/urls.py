from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_request, name='submit_request'),
    path('tracking/', views.request_tracking, name='request_tracking'),
    path('support/', views.support_management, name='support_management'),
    path('response/<int:request_id>/', views.provide_response, name='provide_response'),
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('support_dashboard/', views.support_dashboard, name='support_dashboard'),
    path('login/customer/', views.customer_login, name='customer_login'),
    path('login/support/', views.support_login, name='support_login'),
    path('logout/', views.logout_view, name='logout'),
]