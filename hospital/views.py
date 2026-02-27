from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import User, Doctor, Patient, Appointment, Prescription, Invoice
from .serializers import (
    UserSerializer, DoctorSerializer, PatientSerializer, AppointmentSerializer,
    PrescriptionSerializer, InvoiceSerializer
)
from .permissions import IsAdmin, IsDoctor, IsPatient


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related('doctor__user', 'patient__user').all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(cache_page(60))
    def list(self, request):
        total_revenue = Invoice.objects.aggregate(total=Sum('amount'))['total'] or 0
        upcoming = Appointment.objects.count()
        return Response({'total_revenue': total_revenue, 'appointments_count': upcoming})
