from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm, VehicleCreateForm
from .utils import get_all_vehicles


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = CustomUserCreationForm()
        context['login_form'] = CustomAuthenticationForm()
        return context

    def post(self, request, *args, **kwargs):
        if 'register' in request.POST:  # Идентифицираме заявка за регистрация
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # Автоматично логване след регистрация
                return redirect('front-page')
        elif 'login' in request.POST:  # Идентифицираме заявка за вход
            form = CustomAuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('front-page')
        return self.get(request, *args, **kwargs)


def front_page(request):
    all_vehicles = get_all_vehicles()

    contex = {
        'all_vehicles': all_vehicles
    }

    return render(request, 'front_page.html', contex)


def add_vehicle(request):
    form_vehicle = VehicleCreateForm()

    if request.method == 'POST':
        form_vehicle = VehicleCreateForm(request.POST)
        if form_vehicle.is_valid():
            form_vehicle.save()
            return redirect('front-page')

    context = {
        'form_vehicle': form_vehicle
    }
    return render(request, 'vehicles/add-vehicles.html', context)
