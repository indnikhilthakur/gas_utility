from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, CustomerSupportInteraction
from .forms import ServiceRequestForm, CustomerSupportForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page or any other desired URL

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_customer:  # Adjust the condition based on your user model
            login(request, user)
            return redirect('customer_dashboard')  # Redirect to customer dashboard
        else:
            # Handle invalid login
            pass
    return render(request, 'gas_service/login.html')

def support_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_support_staff:  # Adjust the condition based on your user model
            login(request, user)
            return redirect('gas_service/support_dashboard')  # Redirect to support dashboard
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'gas_service/submit_request.html', {'form': form})

@login_required
def request_tracking(request):
    user = request.user
    requests = ServiceRequest.objects.filter(user=user)
    return render(request, 'gas_service/request_tracking.html', {'requests': requests})

@login_required
def support_management(request):
    if request.user.is_staff:
        requests = ServiceRequest.objects.all()
        return render(request, 'gas_service/support_management.html', {'requests': requests})
    else:
        return redirect('request_tracking')

@login_required
def provide_response(request, request_id):
    service_request = ServiceRequest.objects.get(pk=request_id)
    if request.method == 'POST':
        form = CustomerSupportForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.user = request.user
            interaction.service_request = service_request
            interaction.save()
            service_request.status = 'Resolved'
            service_request.resolved_at = interaction.created_at
            service_request.save()
            return redirect('support_management')
    else:
        form = CustomerSupportForm()
    return render(request, 'gas_service/provide_response.html', {'form': form, 'service_request': service_request})

@login_required
def customer_dashboard(request):
    user = request.user
    requests = ServiceRequest.objects.filter(user=user)
    return render(request, 'gas_service/customer_dashboard.html', {'requests': requests})

@login_required
def support_dashboard(request):
    if request.user.is_staff:
        requests = ServiceRequest.objects.all()
        return render(request, 'gas_service/support_dashboard.html', {'requests': requests})
    else:
        return redirect('customer_dashboard')