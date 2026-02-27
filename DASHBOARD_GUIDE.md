# ApolloCare - Dashboard System Guide

## Overview
A complete role-based dashboard system has been implemented with three distinct user dashboards: **Admin**, **Doctor**, and **Patient**. Each dashboard provides tailored information based on the user's role.

---

## Dashboard Access

### Main Dashboard URL
```
http://127.0.0.1:8000/dashboard/
```

The dashboard automatically redirects users to the appropriate dashboard based on their role.

---

## Admin Dashboard

### Features
- **View Summary Stats**
  - Total number of doctors
  - Total number of patients
  - Total number of appointments
  - System status overview

- **View Recent Appointments**
  - List of all appointments with doctor and patient names
  - Scheduled date and time
  - Appointment reason
  - Quick access to appointment details

- **Manage All Doctors**
  - Complete list of all doctors in the system
  - Name, specialty, and email information
  - Quick access to manage doctors

- **Manage All Patients**
  - Complete list of all patients in the system
  - Number of appointments per patient
  - Quick access to manage patients

- **Quick Actions**
  - Manage Doctors button
  - Manage Patients button
  - View All Appointments button

### Admin Credentials (Demo)
```
Username: admin
Password: adminpass
Email: admin@example.com
```

---

## Doctor Dashboard

### Features
- **Doctor Profile Info**
  - Display doctor's full name
  - Show specialty/department
  - Online status indicator

- **Doctor Statistics**
  - Total number of assigned patients
  - Total number of appointments
  - Active status badge

- **My Appointments**
  - View all appointments assigned to this doctor
  - See patient names and contact information
  - View appointment date, time, and reason
  - See completion status (Pending/Completed)
  - Quick links to appointment details

- **My Patients List**
  - View all patients assigned to this doctor
  - See patient names and email addresses
  - View number of appointments per patient
  - Quick navigation to patient profiles

### Sample Doctor Login Credentials (from demo data)
The system now contains 10 demo doctors. You can login with:
```
Username: doctor1, doctor2, doctor3, ... doctor10
Password: Same as username (auto-generated in demo script)
Example: doctor_1, doctor_2, etc. (check database)
```

---

## Patient Dashboard

### Features
- **Patient Welcome Message**
  - Personalized greeting with patient's full name
  - "Your health is our priority" message

- **Patient Statistics**
  - Total number of assigned doctors
  - Total number of scheduled appointments

- **My Appointments Section**
  - Complete list of all patient appointments
  - Doctor information for each appointment
  - Appointment date and time
  - Reason for visit
  - Appointment status (Upcoming/Completed)
  - Quick view button for each appointment

- **My Doctors List**
  - View all doctors assigned to patient
  - Doctor profile information
  - Doctor specialty/department
  - Doctor contact email
  - Quick navigation to doctor profiles

- **Quick Actions Sidebar**
  - "Book New Appointment" - Create new appointment
  - "Browse All Doctors" - View all available doctors
  - "View All Appointments" - See complete appointment history

### Sample Patient Login Credentials (from demo data)
The system now contains 20 demo patients. You can login with:
```
Username: patient1, patient2, ... patient20
Password: Same as username (auto-generated in demo script)
Example: patient_1, patient_2, etc. (check database)
```

---

## Navigation Updates

### Updated Navbar
The navigation bar has been enhanced with:

1. **Hospital Icon** - Visual identity in the brand logo
2. **Conditional Navigation** - Different menu items for authenticated vs non-authenticated users
3. **User Dropdown Menu** - For authenticated users showing:
   - User's full name
   - User's role badge with icon:
     - 🔐 Admin
     - 🩺 Doctor
     - ❤️ Patient
   - Dashboard link
   - Logout option

### Navigation Flow
```
ApolloCare Logo → Home, Doctors, Appointments, Patients
↓
If Logged In:
  → User Dropdown (Name + Role Badge)
    → Dashboard (Role-based)
    → Logout

If Not Logged In:
  → Sign In Button
```

---

## User Types & Access

### 1. ADMIN
- **Access Level**: Full system access
- **Can View**: All patients, doctors, and appointments
- **Can Edit**: User profiles, doctor assignments
- **Dashboard Shows**: System-wide analytics and management tools

### 2. DOCTOR
- **Access Level**: Limited to assigned patients and appointments
- **Can View**: Only their assigned patients and appointments
- **Can See**: Patient details and appointment history
- **Dashboard Shows**: Patient list and appointment schedule

### 3. PATIENT
- **Access Level**: Limited to own profile and appointments
- **Can View**: Only their own appointments and assigned doctors
- **Can Book**: New appointments
- **Dashboard Shows**: Doctor list and appointment schedule

---

## Key Views (URLs)

| URL | View | Accessible By |
|-----|------|---|
| `/` | Home Page | Everyone |
| `/dashboard/` | Role-based Dashboard | Authenticated Users |
| `/admin_dashboard/` | Admin Dashboard | Admins |
| `/doctor_dashboard/` | Doctor Dashboard | Doctors |
| `/patient_dashboard/` | Patient Dashboard | Patients |
| `/doctors/` | All Doctors | Everyone |
| `/doctors/<id>/` | Doctor Detail | Everyone |
| `/patients/` | All Patients | Staff |
| `/patients/<id>/` | Patient Detail | Staff & Own Profile |
| `/appointments/` | All Appointments | Everyone |
| `/appointments/create/` | Book Appointment | Authenticated Patients |
| `/appointments/<id>/` | Appointment Detail | Related Users |
| `/login/` | Login | Everyone |
| `/logout/` | Logout | Authenticated Users |

---

## Database Demo Data

The system now includes:
- **10 Demo Doctors** with various specialties
- **20 Demo Patients** with booking history
- **Multiple Appointments** demonstrating the booking system

To repopulate demo data, run:
```bash
python manage.py populate_demo
```

---

## Testing the Dashboards

### Step 1: Login as Admin
1. Navigate to http://127.0.0.1:8000/login/
2. Enter admin credentials (username: admin, password: adminpass)
3. Click "Dashboard" → see admin dashboard with all system data

### Step 2: Login as Doctor
1. Logout from current session
2. Navigate to http://127.0.0.1:8000/login/
3. Enter a doctor credential (e.g., doctor1)
4. Click "Dashboard" → see doctor dashboard with assigned patients

### Step 3: Login as Patient
1. Logout from current session
2. Navigate to http://127.0.0.1:8000/login/
3. Enter a patient credential (e.g., patient1)
4. Click "Dashboard" → see patient dashboard with appointments and doctors

---

## Created/Modified Files

### New Templates
- `templates/admin_dashboard.html` - Admin dashboard
- `templates/doctor_dashboard.html` - Doctor dashboard
- `templates/patient_dashboard.html` - Patient dashboard

### Modified Files
- `apps/patients/views.py` - Added 4 new dashboard view functions
- `apps/patients/urls.py` - Added dashboard route
- `templates/base.html` - Updated navbar with dropdowns and role badges

### Views Created in apps/patients/views.py
```python
def dashboard(request)          # Main router view
def admin_dashboard(request)    # Admin dashboard
def doctor_dashboard(request)   # Doctor dashboard
def patient_dashboard(request)  # Patient dashboard
```

---

## Features & Styling

### Visual Design
- Clean, modern Bootstrap 5 interface
- Card-based layouts for information grouping
- Icons from Bootstrap Icons library
- Color-coded badges for status (success, info, warning, danger)
- Responsive tables with hover effects
- Smooth transitions and animations

### Data Visualization
- Statistics cards with icons
- Progress bars for metrics
- Appointment lists with timestamps
- Patient/doctor lists with contact info
- Status badges (Pending, Complete, Online, etc.)

### User Experience
- Role-based navigation
- Quick action buttons
- Breadcrumb navigation through cards
- Search and filter capabilities
- Mobile-responsive design

---

## Security Features

- Login required for all dashboards (@login_required decorator)
- Role-based access control (RBAC)
- Users can only see data relevant to their role
- Patient data protected from other patients
- Doctor can only see assigned patients

---

## Future Enhancements

Potential improvements for future versions:
1. Advanced filtering and search in dashboards
2. Export appointment data to PDF/CSV
3. SMS/Email notifications for appointments
4. Doctor availability calendar view
5. Patient health records management
6. Prescription history view
7. Invoice/payment tracking
8. Appointment reminders
9. Doctor ratings and reviews
10. Appointment rescheduling functionality

---

## Support & Troubleshooting

### Dashboard Not Loading
- Ensure you are logged in
- Check browser console for errors
- Verify database has demo data

### Missing Patient/Doctor Data
- Run `python manage.py populate_demo` to add demo data
- Check that appointments are created with both doctor and patient

### Navigation Issues
- Clear browser cache
- Try logging out and back in
- Verify role is set correctly in database

---

## Summary

This comprehensive dashboard system provides:
✅ Role-based user interfaces (Admin, Doctor, Patient)
✅ Different data visibility based on user role
✅ Quick access to relevant information
✅ Professional, modern UI design
✅ Full appointment and patient management
✅ Doctor specialization tracking
✅ Responsive and mobile-friendly layout

The system is now ready for testing with the demo data population in place!
