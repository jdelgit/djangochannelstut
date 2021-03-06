from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})


def room(request, *args, **kwargs):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(kwargs['room_name']))
    })