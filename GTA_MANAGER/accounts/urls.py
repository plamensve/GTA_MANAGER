from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from .views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('test/', views.test, name='test'),
)
