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
)
