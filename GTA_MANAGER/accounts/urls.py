from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('profile-page/', views.profile_page, name='profile-page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('front-page/', views.front_page, name='front-page'),
    path('account/add-vehicle/', views.add_vehicle, name='add-vehicle'),
    path('edit-profile-page/', views.edit_profile_page, name='edit-profile-page'),
    path('vehicles/<int:pk>/', views.vehicle_details, name='vehicle_details'),
    path('vehicles/<int:pk>/add-full-information', views.add_full_information, name='add-full-information'),
    path('vehicles/<int:pk>/edit-information', views.edit_full_information, name='edit-information'),
    path('vehicles/<int:pk>/delete-information', views.delete_information, name='delete-information'),
    path('generate-report/', views.generate_vehicle_report, name='generate_report'),
    path('generate-report-info/', views.generate_vehicle_report_info, name='generate_report'),
    path('send-email/', views.send_email, name='send_email'),
    path('after-register/', views.after_register, name='after-register'),
)
