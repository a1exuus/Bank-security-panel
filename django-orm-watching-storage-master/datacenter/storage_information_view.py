from datacenter.models import Visit
from django.shortcuts import render
from datacenter.visit_utils import get_duration, format_duration


def storage_information_view(request):
    active_visitors = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visitor in active_visitors:
        name = visitor.passcard
        duration, entered_at = get_duration(visitor)
        duration = format_duration(duration)

        visitor_dict = {
            'who_entered': name,
            'entered_at': entered_at,
            'duration': duration,
        }

        non_closed_visits.append(visitor_dict)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    
    return render(request, 'storage_information.html', context)
