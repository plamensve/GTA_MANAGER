from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.contrib.auth import login
from openpyxl.styles import Font, Alignment, Border, Side

from .forms import CustomUserCreationForm, CustomAuthenticationForm, VehicleCreateForm, CustomUserChangeForm, \
    VehicleFullDetailsCreateForm, VehicleEditForm
from .models import Vehicles, VehicleFullDetails
from .utils import get_all_vehicles, vehicle_full_details_info
from openpyxl import Workbook

from ..web.utils import check_expiration, send_email_registration


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
                return redirect('after-register')
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


@login_required(login_url='index')
def front_page(request):
    all_vehicles = get_all_vehicles()
    current_user = request.user

    contex = {
        'all_vehicles': all_vehicles,
        'current_user': current_user,
    }

    if current_user.is_authenticated:
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


@login_required(login_url='index')
def vehicle_details(request, pk):
    vehicle_details = vehicle_full_details_info(pk)
    vehicle_information = VehicleFullDetails.objects.filter(vehicle_id=pk).first()

    try:
        current_vehicle = Vehicles.objects.get(pk=pk)
    except Vehicles.DoesNotExist:
        return render(request, '404.html', status=404)

    condition_class = 'status-active' if current_vehicle.condition == 'АКТИВЕН' else 'status-inactive'

    context = {
        'current_vehicle': current_vehicle,
        'condition_class': condition_class,
        'vehicle_details': vehicle_details,
        'vehicle_information': vehicle_information if vehicle_information else None,
    }

    return render(request, 'vehicles/vehicle-details.html', context)


@login_required(login_url='index')
def add_full_information(request, pk):
    vehicle = get_object_or_404(Vehicles, pk=pk)

    if request.method == 'POST':
        form = VehicleFullDetailsCreateForm(request.POST)
        if form.is_valid():
            vehicle_full_details = form.save(commit=False)
            vehicle_full_details.vehicle = vehicle
            vehicle_full_details.save()
            return redirect('vehicle_details', pk=pk)
    else:
        form = VehicleFullDetailsCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'vehicles/add-full-information.html', context)


@login_required(login_url='index')
def edit_full_information(request, pk):
    vehicle_full_details = get_object_or_404(Vehicles, pk=pk)
    vehicle_second_full_details = get_object_or_404(VehicleFullDetails, vehicle_id=pk)

    if request.method == 'POST':
        form = VehicleEditForm(request.POST, instance=vehicle_full_details)
        form_2 = VehicleFullDetailsCreateForm(request.POST, instance=vehicle_second_full_details)

        if form.is_valid() and form_2.is_valid():
            # Save the first form
            form.save()

            # Save the second form with a ForeignKey to vehicle_full_details
            second_details = form_2.save(commit=False)
            second_details.vehicle = vehicle_full_details  # Свързване на ForeignKey
            second_details.save()

            return redirect('vehicle_details', pk=pk)
    else:
        form = VehicleEditForm(instance=vehicle_full_details)
        form_2 = VehicleFullDetailsCreateForm(instance=vehicle_second_full_details)

    context = {
        'form': form,
        'form_2': form_2,
        'vehicle_full_details': vehicle_full_details,
    }

    return render(request, 'vehicles/edit-full-information.html', context)


@login_required(login_url='index')
def delete_information(request, pk):
    vehicle_full_details = get_object_or_404(Vehicles, pk=pk)

    if request.method == 'POST':
        vehicle_full_details.delete()
        return redirect('front-page')

    # Ако е GET заявка, покажете страницата за потвърждение
    return render(request, 'vehicles/delete-information.html', {'vehicle': vehicle_full_details})


@login_required(login_url='index')
def generate_vehicle_report(request):
    # Създаване на Excel файл
    wb = Workbook()
    ws = wb.active
    ws.title = "Служебни превозни средства"

    # Стилове
    bold_font = Font(bold=True, size=14)
    center_alignment = Alignment(horizontal='center', vertical='center')
    border = Border(
        left=Side(border_style='thin'),
        right=Side(border_style='thin'),
        top=Side(border_style='thin'),
        bottom=Side(border_style='thin')
    )

    # Добавяне на заглавия
    header_info = 'ДЖИ ТИ ЕЙ ПЕТРОЛИУМ ООД - АВТОМОБИЛИ / ВЛЕКАЧИ / ЦИСТЕРНИ'
    ws.append([header_info])
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=6)  # Обединяване на клетките
    header_cell = ws.cell(row=1, column=1)
    header_cell.font = Font(bold=True, size=16)
    header_cell.alignment = center_alignment

    headers = ["№", "Тип", "Марка", "Модел", "Рег. номер", "Състояние"]
    ws.append(headers)

    for col_num, header in enumerate(headers, start=1):
        cell = ws.cell(row=2, column=col_num)
        cell.font = bold_font
        cell.alignment = center_alignment
        cell.border = border

    # Добавяне на данни от базата
    all_vehicles = Vehicles.objects.all()
    for idx, vehicle in enumerate(all_vehicles, start=1):
        row = [
            idx,
            vehicle.type.upper(),
            vehicle.brand.upper(),
            vehicle.model.upper(),
            vehicle.register_number.upper(),
            vehicle.condition.upper()
        ]
        ws.append(row)

        for col_num, value in enumerate(row, start=1):
            cell = ws.cell(row=idx + 2, column=col_num)
            cell.alignment = center_alignment
            cell.border = border

    # Настройки за ширина на колоните
    column_widths = [10, 20, 25, 25, 30, 20]  # Увеличени ширини
    for i, width in enumerate(column_widths, start=1):
        ws.column_dimensions[chr(64 + i)].width = width

    # Настройки за отговор
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="vehicle_report.xlsx"'

    # Запазване на Excel файла в отговора
    wb.save(response)
    return response


def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        # Вашата логика за изпращане на имейл
        expiration_documents = check_expiration()

        documents_list = [
            {
                'current_registration_number': docs['current_registration_number'],
                'insurance_civil_liability': docs['insurance_civil_liability'],
                'insurance_casco_validity': docs['insurance_casco_validity'],
                'tachograph_validity': docs['tachograph_validity'],
                'adr_validity': docs['adr_validity'],
                'fitness_protocol_validity': docs['fitness_protocol_validity'],
                'technical_check_validity': docs['technical_check_validity'],
            }
            for docs in expiration_documents
        ]

        html_message = render_to_string('email_templates/expiration_email.html', {
            'documents_list': documents_list,
        })

        send_mail(
            subject="Обобщена информация за изтичащи документи",
            message=None,
            from_email='svetoslavov.plamen@gmail.com',
            recipient_list=[email],
            html_message=html_message,
        )
        return JsonResponse({'success': 'Email sent successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def after_register(request):
    return render(request, 'after-register.html')
