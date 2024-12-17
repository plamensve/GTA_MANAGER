from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', views.front_page, name='front-page'),
    path('account/add-vehicle/', views.add_vehicle, name='add-vehicle'),
)
