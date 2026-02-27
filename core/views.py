from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from hospital.models import Doctor, User
from hospital.models import Invoice, Appointment
from django.db.models import Sum


def home(request):
    doctors = Doctor.objects.select_related('user').all()[:8]
    return render(request, 'home.html', {'doctors': doctors})


def login_portal(request):
    """Login portal page where users choose their role"""
    return render(request, 'login_portal.html')


def admin_login(request):
    """Admin-specific login page"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.role == 'admin':
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'This account is not an Admin account. Please use the correct login page.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'admin_login.html')


def doctor_login(request):
    """Doctor-specific login page"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.role == 'doctor':
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'This account is not a Doctor account. Please use the correct login page.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'doctor_login.html')


def patient_login(request):
    """Patient-specific login page"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.role == 'patient':
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'This account is not a Patient account. Please use the correct login page.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'patient_login.html')


@login_required
def admin_dashboard(request):
    total_revenue = Invoice.objects.aggregate(total=Sum('amount'))['total'] or 0
    appointments_count = Appointment.objects.count()
    unpaid = Invoice.objects.filter(paid=False).count()
    return render(request, 'admin_dashboard.html', {'total_revenue': total_revenue, 'appointments_count': appointments_count, 'unpaid_invoices': unpaid})
