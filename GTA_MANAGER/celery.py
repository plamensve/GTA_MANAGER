from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Задаване на настройките за Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GTA_MANAGER.settings')

# Създаване на Celery приложение
app = Celery('GTA_MANAGER')

# Зареждане на Celery конфигурацията от Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматично откриване на задачи в приложенията
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'run-my-task-every-minute': {
        'task': 'GTA_MANAGER.web.tasks.send_email_task',
        'schedule': crontab(day_of_month='1,15', hour='7', minute='00'),
        'args': ('Служебни превозни средства, камиони и цистерни - краен срок за подновяване на документите',
                 'Test Message', ['svetoslavov.plamen@gmail.com']),
    },
}

# Настройване на времевата зона
app.conf.timezone = 'UTC'

# Примерна задача за дебъгване
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
