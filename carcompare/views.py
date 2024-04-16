from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Car

import json

def index(request):
    car_list = Car.objects.all()
    # template = loader.get_template('index.html')
    #return HttpResponse(template.render())
    #output = ", ".join([q.car_name for q in car_list])
    #return HttpResponse(output)

    template = loader.get_template("index.html")
    context = {
        "car_list": car_list,
    }
    return HttpResponse(template.render(context, request))

def filter(request):
    car_list = []
    template = loader.get_template("index.html")
    car_full_list = Car.objects.all()
    if 'ncap' in request.POST.keys():
        for car in car_full_list:
            if int(car.ncap_rating) >= 4:
                car_list.append(car)
    elif 'sedan' in request.POST.keys():
        for car in car_full_list:
            if car.car_type == 'Sedan':
                car_list.append(car)
    elif 'suv' in request.POST.keys():
        for car in car_full_list:
            if car.car_type == 'Compact SUV':
                car_list.append(car)
    context = {
            "car_list": car_list,
        }

    return HttpResponse(template.render(context, request))


def car_data():
    
    data = '''
    {
        "Nexon":{
        "Manufacture": "Tata",
        "NCAP": "Global NCAP",
        "Rating" : "5"
        }
    }
    '''

    return data