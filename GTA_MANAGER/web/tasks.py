import os

from django.core.mail import send_mail
from django.template.loader import render_to_string

from GTA_MANAGER import settings
from GTA_MANAGER.celery import app


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from GTA_MANAGER.celery import app
from GTA_MANAGER.web.utils import check_expiration


@app.task
def send_email_task(subject, message, recipient_list):

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

    html_content = render_to_string(settings.HTML_FILE_PATH, {
        'documents_list': documents_list
    })

    send_mail(
        subject,
        message,
        'svetoslavov.dev@gmail.com',  # Подател
        recipient_list,
        fail_silently=False,
        html_message=html_content,  # Рендерирано HTML съдържание
    )


