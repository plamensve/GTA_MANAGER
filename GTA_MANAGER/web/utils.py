import time
from datetime import date

from django.core.mail import send_mail
from django.http import HttpResponse

from GTA_MANAGER.accounts.models import VehicleFullDetails, Vehicles


def send_test_email():
    expiration_documents = check_expiration()

    for docs in expiration_documents:
        send_mail(
            subject=f"Документите на {docs['current_registration_number']} изтичат",
            message=(
                f"Застраховка Гражданска Отговорност изтича след {docs['insurance_civil_liability'].days} дни.\n"
                f"Застраховка КАСКО изтича след {docs['insurance_casco_validity'].days} дни.\n"
                f"След {docs['tachograph_validity'].days} дни изтича прегледа на тахографа.\n"
                f"АДР валидност още {docs['adr_validity'].days} дни.\n"
                f"Протоколът за годност изтича след {docs['fitness_protocol_validity'].days} дни.\n"
                f"Техническият преглед изтича след {docs['technical_check_validity'].days} дни.\n"
                f"Този e-mail се генерира автоматично и ще го получавате в началото на всеки месец."
            ),
            from_email='svetoslavov.plamen@gmail.com',
            recipient_list=['svetoslavov.dev@gmail.com'],
        )
    return HttpResponse('Emails sent successfully!')


def check_expiration():
    current_expiration_insurances = VehicleFullDetails.objects.all()
    today = date.today()
    results = []

    for ins in current_expiration_insurances:
        insurance_civil_liability_result = ins.insurance_civil_liability - today
        insurance_casco_validity_result = ins.insurance_casco_validity - today
        tachograph_validity_result = ins.tachograph_validity - today
        adr_validity_result = ins.adr_validity - today
        fitness_protocol_validity_result = ins.fitness_protocol_validity - today
        technical_check_validity_result = ins.technical_check_validity - today

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
