from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<int:nurse_id>/<str:date>/', views.DashboardView.as_view(), name='dashboard'),
    path('add_checkup_data/', views.CheckupDataEntryView.as_view(), name='add_checkup_data'),
    path('resident_condition/', views.ResidentConditionView.as_view(), name='resident_condition'),
]
