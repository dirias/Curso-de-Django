#Django
import builtins
from django.http import HttpResponse, JsonResponse #Para devolver peticiones, Devolver en formato Json
# Utilities
from datetime import date, datetime



def hello_word(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'This is the current server time -> {str(now)}')

def hi(request):
    """Hi"""
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    dict = {"Key " + element: element for element in sorted(numbers)} 
    return JsonResponse(dict)
def say_hi(request, name, age):
    if age < 12:
        message = f'Sorry {name}, you are not allowed here.'
    else:
        message = f'Hello, {name}! Welcome to Platzigram'
    return HttpResponse(message)