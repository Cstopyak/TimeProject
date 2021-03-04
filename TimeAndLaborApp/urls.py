from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path("registerPage", views.registerPage),
    path("Login", views.Login),
    path("UserDashboard", views.UserDashboard),
    path("logout", views.logout),
    path("registerProcess", views.registerProcess),
    path("MyBenefits", views.MyBenefits),
    path("SettingsPage", views.SettingsPage),
    path("MyReports", views.MyReports),
    path("requestTimeOff", views.requestTimeOff),
    path("clockIn", views.clockIn),
    path("clockOut", views.clockOut),
    
]