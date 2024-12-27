import time
from datetime import date
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from GTA_MANAGER.accounts.models import VehicleFullDetails, Vehicles
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponse


def send_email_registration(email):
    expiration_documents = check_expiration()

    # Създаваме списък за всички превозни средства
    documents_list = []
    for docs in expiration_documents:
        documents_list.append({
            'current_registration_number': docs['current_registration_number'],
            'insurance_civil_liability': docs['insurance_civil_liability'],
            'insurance_casco_validity': docs['insurance_casco_validity'],
            'tachograph_validity': docs['tachograph_validity'],
            'adr_validity': docs['adr_validity'],
            'fitness_protocol_validity': docs['fitness_protocol_validity'],
            'technical_check_validity': docs['technical_check_validity'],
        })

    # Рендерираме един HTML шаблон с всички документи
    html_message = render_to_string('email_templates/expiration_email.html', {
        'documents_list': documents_list,
    })

    # Изпращаме само един имейл
    send_mail(
        subject="Обобщена информация за изтичащи документи",
        message=None,  # Оставяме текстовото съобщение празно
        from_email='svetoslavov.plamen@gmail.com',
        recipient_list=[email],
        html_message=html_message,
    )
    return HttpResponse('Email sent successfully!')


def check_expiration():
    current_expiration_insurances = VehicleFullDetails.objects.all()
    results = []

    for ins in current_expiration_insurances:
        insurance_civil_liability_result = None
        insurance_casco_validity_result = None
        tachograph_validity_result = None
        adr_validity_result = None
        fitness_protocol_validity_result = None
        technical_check_validity_result = None

        if ins.insurance_civil_liability:
            insurance_civil_liability_result = ins.insurance_civil_liability
        if ins.insurance_casco_validity:
            insurance_casco_validity_result = ins.insurance_casco_validity
        if ins.tachograph_validity:
            tachograph_validity_result = ins.tachograph_validity
        if ins.adr_validity:
            adr_validity_result = ins.adr_validity
        if ins.fitness_protocol_validity:
            fitness_protocol_validity_result = ins.fitness_protocol_validity
        if ins.technical_check_validity:
            technical_check_validity_result = ins.technical_check_validity

        current_number = get_current_vehicle(ins.vehicle_id)
        current_registration_number = current_number.register_number.upper()

        result = {
            'current_registration_number': current_registration_number,
            'insurance_civil_liability': insurance_civil_liability_result,
            'insurance_casco_validity': insurance_casco_validity_result,
            'tachograph_validity': tachograph_validity_result,
            'adr_validity': adr_validity_result,
            'fitness_protocol_validity': fitness_protocol_validity_result,
            'technical_check_validity': technical_check_validity_result,
        }

        results.append(result)

    return results


def get_current_vehicle(vehicle_id):
    current_vehicle = Vehicles.objects.get(pk=vehicle_id)
    return current_vehicle
