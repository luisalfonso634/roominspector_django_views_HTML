#RoomInspector Views
#Django

from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hola Room Service, la hora actual del servidor es {now}'.format(now=now))

def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status':'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )
def say_hi(request, name, age):
    if age < 18:
        message = 'Sorry {}, you are too young for us'.format(name)
    else:
        message = "Hello, {}! Welcome to RoomInspector".format(name)
    return HttpResponse(message)



