from django.shortcuts import render, get_object_or_404, redirect
from hospital.models import Appointment, Patient, Doctor, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm
from hospital.forms import PrescriptionForm, InvoiceForm


@login_required
def doctors_list(request):
    doctors = Doctor.objects.select_related('user').all()
    return render(request, 'doctors_list.html', {'doctors': doctors})


@login_required
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor_detail.html', {'doctor': doctor})


@login_required
def patients_list(request):
    patients = Patient.objects.select_related('user').all()
    return render(request, 'patients_list.html', {'patients': patients})


@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient_detail.html', {'patient': patient})


@login_required
def appointment_prescription_create(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            pres = form.save(commit=False)
            pres.appointment = appt
            pres.save()
            return redirect('appointment_detail', pk=pk)
    else:
        form = PrescriptionForm()
    return render(request, 'prescription_form.html', {'form': form, 'appointment': appt})


@login_required
def appointment_invoice_create(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            inv = form.save(commit=False)
            inv.appointment = appt
            inv.save()
            return redirect('appointment_detail', pk=pk)
    else:
        form = InvoiceForm()
    return render(request, 'invoice_form.html', {'form': form, 'appointment': appt})


@login_required
def appointment_list(request):
    appointments = Appointment.objects.select_related('doctor__user', 'patient__user').all()
    return render(request, 'appointment_list.html', {'appointments': appointments})


@login_required
def appointment_detail(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointment_detail.html', {'appointment': appt})


def appointment_create(request):
    """Allow anonymous users and patients to book appointments (not admins or doctors)"""
    
    # Check if authenticated user is admin or doctor - they cannot book
    if request.user.is_authenticated and request.user.role in ['admin', 'doctor']:
        messages.error(request, f'{request.user.role.capitalize()}s cannot book appointments. Access denied.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            
            # If user is authenticated, use their patient profile
            if request.user.is_authenticated:
                patient = getattr(request.user, 'patient_profile', None)
                if not patient:
                    patient = Patient.objects.create(user=request.user)
                appt.patient = patient
            else:
                # For anonymous users, create a basic patient profile
                # First check if a patient with this email exists
                patient_name = request.POST.get('patient_name')
                patient_email = request.POST.get('patient_email')
                
                if patient_name and patient_email:
                    # Try to find or create a user for this guest
                    try:
                        user = User.objects.get(email=patient_email)
                    except User.DoesNotExist:
                        # Create a guest user
                        username = patient_email.split('@')[0]
                        user = User.objects.create_user(
                            username=username,
                            email=patient_email,
                            first_name=patient_name.split()[0] if patient_name else 'Guest',
                            role='patient'
                        )
                    
                    patient = getattr(user, 'patient_profile', None)
                    if not patient:
                        patient = Patient.objects.create(user=user)
                    appt.patient = patient
                else:
                    messages.error(request, 'Please provide your name and email to book an appointment.')
                    return render(request, 'appointment_create.html', {'form': form})
            
            appt.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('appointment_detail', pk=appt.pk)
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment_create.html', {'form': form})


@login_required
def appointment_cancel(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appt.delete()
        return redirect('appointment_list')
    return render(request, 'appointment_cancel.html', {'appointment': appt})


@login_required
def dashboard(request):
    """Main dashboard that redirects based on user role"""
    user = request.user
    
    if user.role == 'admin':
        return admin_dashboard(request)
    elif user.role == 'doctor':
        return doctor_dashboard(request)
    else:  # patient
        return patient_dashboard(request)


@login_required
def admin_dashboard(request):
    """Admin dashboard showing all appointments, patients, and doctors"""
    appointments = Appointment.objects.select_related('doctor__user', 'patient__user').all()
    patients = Patient.objects.select_related('user').all()
    doctors = Doctor.objects.select_related('user').all()
    
    context = {
        'appointments': appointments,
        'patients': patients,
        'doctors': doctors,
        'total_appointments': appointments.count(),
        'total_patients': patients.count(),
        'total_doctors': doctors.count(),
    }
    return render(request, 'admin_dashboard.html', context)


@login_required
def doctor_dashboard(request):
    """Doctor dashboard showing their patients and appointments"""
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return redirect('home')
    
    appointments = Appointment.objects.filter(doctor=doctor).select_related('patient__user')
    patients = Patient.objects.filter(appointments__doctor=doctor).distinct()
    
    context = {
        'doctor': doctor,
        'appointments': appointments,
        'patients': patients,
        'total_appointments': appointments.count(),
        'total_patients': patients.count(),
    }
    return render(request, 'doctor_dashboard.html', context)


@login_required
def patient_dashboard(request):
    """Patient dashboard showing their doctor and appointments"""
    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        patient = Patient.objects.create(user=request.user)
    
    appointments = Appointment.objects.filter(patient=patient).select_related('doctor__user')
    doctors = Doctor.objects.filter(appointments__patient=patient).distinct()
    
    context = {
        'patient': patient,
        'appointments': appointments,
        'doctors': doctors,
        'total_appointments': appointments.count(),
    }
    return render(request, 'patient_dashboard.html', context)

