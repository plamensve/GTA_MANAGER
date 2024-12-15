from django.urls import path

from GTA_MANAGER.web import views

urlpatterns = (
    path('', views.index, name='index'),
)