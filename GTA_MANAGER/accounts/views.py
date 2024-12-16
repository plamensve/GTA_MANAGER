from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm


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
                return redirect('test')
        elif 'login' in request.POST:  # Идентифицираме заявка за вход
            form = CustomAuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('test')
        return self.get(request, *args, **kwargs)


def test(request):
    return render(request, 'test.html')
