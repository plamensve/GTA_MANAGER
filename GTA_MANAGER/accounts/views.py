from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm, VehicleCreateForm, CustomUserChangeForm
from .utils import get_all_vehicles


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            register_form = CustomUserCreationForm(self.request.POST)
            form_invalid = not register_form.is_valid()
        else:
            register_form = CustomUserCreationForm()
            form_invalid = False

        login_form = CustomAuthenticationForm()

        context['register_form'] = register_form
        context['login_form'] = login_form
        context['form_invalid'] = form_invalid
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if 'register' in request.POST:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('front-page')
            else:
                context['register_form'] = form  # Връща формата с грешки обратно в контекста

        elif 'login' in request.POST:
            form = CustomAuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('front-page')
            else:
                context['login_form'] = form  # Връща формата с грешки обратно в контекста

        return self.render_to_response(context)


@login_required()
def front_page(request):
    all_vehicles = get_all_vehicles()
    current_user = request.user

    contex = {
        'all_vehicles': all_vehicles,
        'current_user': current_user
    }

    return render(request, 'front_page.html', contex)


@login_required(login_url='index')
def profile_page(request):
    current_user = request.user

    contex = {
        'current_user': current_user
    }

    return render(request, 'profile-page.html', contex)


@login_required(login_url='index')
def edit_profile_page(request):
    current_user = request.user

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('profile-page')  # Пренасочване след редакция
    else:
        form = CustomUserChangeForm(instance=current_user)  # Зарежда текущите данни на потребителя

    context = {
        'form': form,
        'current_user': current_user
    }

    return render(request, 'edit-profile-page.html', context)


@login_required(login_url='index')
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
