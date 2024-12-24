from datetime import timedelta


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
    return get_duration(visit) >= timedelta(minutes=minutes)