"""
URL configuration for belasheshe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from nurse.views import nurse_dashboard
from doctors.views import doctor_dashboard
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nurse/dashboard/', nurse_dashboard, name='nurse_dashboard'),
    path('doctors/dashboard/', doctor_dashboard, name='doctors_dashboard'),
    path('residents/', include('residents.urls'))
]
