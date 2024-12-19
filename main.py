import os

import django

from django.utils.timezone import localtime

from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit


def get_duration(visit):
    entered_at = visit.entered_at
    leaved_at = visit.leaved_at
    if leaved_at:
        delta = leaved_at - entered_at
        return delta


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    formatted_delta = f"{hours:02}:{minutes:02}:{seconds:02}"
    return formatted_delta


def is_visit_long(visit, minutes=60):
    if get_duration(visit) >= timedelta(minutes=minutes):
        return True
    return False


if __name__ == '__main__':
    passcards = Passcard.objects.all()
    active_users = Visit.objects.filter(leaved_at=None)
    for user in active_users:
        then = user.entered_at + timedelta(hours=3)
        now = localtime()
        delta = now - then
        total_seconds = int(delta.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        formatted_delta = f"{hours:02}:{minutes:02}:{seconds:02}"
    # for visitor in active_users:
        # print(f'Зашёл в хранилище, время по москве:\n{now}\n\nИмя: {visitor.passcard}\n\nНаходится в хранилище: {formatted_delta}')
    visitor = Passcard.objects.all()[0]
    visits = Visit.objects.filter(passcard=visitor)
    suspicious_visits = []
    for visit in visits:
        long_visit_check = is_visit_long(visit)
        if long_visit_check:
            suspicious_visits.append(visit)
    print(f'Визиты дольше 60 минут: {suspicious_visits}')