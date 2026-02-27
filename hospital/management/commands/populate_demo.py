from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from hospital.models import Doctor, Patient
import random

class Command(BaseCommand):
    help = 'Populate database with demo doctors and patients'

    def handle(self, *args, **options):
        User = get_user_model()
        doctor_names = [
            ('Oliver', 'Thompson'), ('Emma', 'Johnson'), ('Liam', 'Williams'),
            ('Ava', 'Brown'), ('Noah', 'Jones'), ('Sophia', 'Garcia'),
            ('Ethan', 'Miller'), ('Isabella', 'Davis'), ('Mason', 'Rodriguez'),
            ('Mia', 'Martinez')
        ]
        patient_names = [
            ('James', 'Anderson'), ('Charlotte', 'Taylor'), ('Benjamin', 'Moore'),
            ('Amelia', 'Jackson'), ('Lucas', 'Martin'), ('Harper', 'Lee'),
            ('Henry', 'Perez'), ('Evelyn', 'Thompson'), ('Alexander', 'White'),
            ('Abigail', 'Harris'), ('Michael', 'Sanchez'), ('Emily', 'Clark'),
            ('Daniel', 'Ramirez'), ('Elizabeth', 'Lewis'), ('Samuel', 'Robinson'),
            ('Sofia', 'Walker'), ('Matthew', 'Young'), ('Avery', 'Allen'),
            ('Joseph', 'King'), ('Madison', 'Wright')
        ]

        # create doctors
        for i, name in enumerate(doctor_names, start=1):
            username = f'doc{i}'
            if not User.objects.filter(username=username).exists():
                first, last = name
                user = User.objects.create_user(
                    username=username,
                    password='test1234',
                    role='doctor',
                    first_name=first,
                    last_name=last,
                    email=f'doc{i}@example.com'
                )
                Doctor.objects.create(user=user, specialty=random.choice(['Cardiology','Dermatology','General','Pediatrics','Neurology']))
        # create patients
        for i, name in enumerate(patient_names, start=1):
            username = f'pat{i}'
            if not User.objects.filter(username=username).exists():
                first, last = name
                user = User.objects.create_user(
                    username=username,
                    password='test1234',
                    role='patient',
                    first_name=first,
                    last_name=last,
                    email=f'pat{i}@example.com'
                )
                Patient.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS('Demo doctors and patients created'))
