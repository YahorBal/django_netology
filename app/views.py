from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Car


def hello(request):
    context = {
        "test" : 5,
        "data": [1,2,3,4,5,6,7],
        "val": 'hello',
    }
    return render(request, 'demo.html', context)


def sum(request, op1,  op2):
    result = op1 + op2
    return HttpResponse(f'Sum = {result}')

CONTENT = [str(i) for i in range(10000)]

def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context )

def create_car(request):
    car = Car(brand='demo', model='demo2', color='demo3')
    car.save()

    return HttpResponse(f'GREAT!, {car.brand}, {car.model}', status=200)


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello World!!!!!!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)