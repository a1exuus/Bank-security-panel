from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration, format_duration, is_visit_long
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcards = Passcard.objects.all()
    passcard = get_object_or_404(passcards ,passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []


    for visit in visits:
        visit_dict = {
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit)
            }
        this_passcard_visits.append(visit_dict)


    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
