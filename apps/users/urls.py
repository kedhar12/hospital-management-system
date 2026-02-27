from django.urls import path
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    # Login portal - choose your role
    path('login/', core_views.login_portal, name='login_portal'),
    
    # Role-specific login pages
    path('login/admin/', core_views.admin_login, name='admin_login'),
    path('login/doctor/', core_views.doctor_login, name='doctor_login'),
    path('login/patient/', core_views.patient_login, name='patient_login'),
    
    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    # Legacy login for compatibility
    path('login/default/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
