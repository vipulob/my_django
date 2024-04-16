from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

import json

def index(request):
    car_list = json.loads(car_data())
    print(car_list)

    #for car in car_list['car_data']:
        

    template = loader.get_template("index.html")
    context = {
        "car_list": car_list,
    }
    return HttpResponse(template.render(context, request))

def car_data():
    
    data = '''
    {
        "car_data" : [
        {"car_name": "City 4th Gen",
        "Manufacturer": "Honda",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 4,
        "Baby": 4,
        "Year": 2022},
        {"car_name": "Carens",
        "Manufacturer": "Kia",
        "NCAP": "Global NCAP",
        "Test": "6 Airbags",
        "Adult" : 3,
        "Baby": 3,
        "Year": 2022},
        {"car_name": "Creta",
        "Manufacturer": "Hyundai",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 3,
        "Baby": 3,
        "Year": 2022},
        {"car_name": "Grand i10 Nios",
        "Manufacturer": "Hyundai",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 2,
        "Baby": 2,
        "Year": 2020},
        {"car_name": "i20",
        "Manufacturer": "Hyundai",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 3,
        "Baby": 3,
        "Year": 2022},
         {"car_name": "Ignis",
        "Manufacturer": "Maruti Suzuki",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 1,
        "Baby": 0,
        "Year": 2022},
        {"car_name": "Jazz",
        "Manufacturer": "Honda",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 4,
        "Baby": 3,
        "Year": 2022},
        {"car_name": "Kiger",
        "Manufacturer": "Renault",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 4,
        "Baby": 2,
        "Year": 2022},
        {"car_name": "Kushaq",
        "Manufacturer": "Skoda",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 5,
        "Baby": 5,
        "Year": 2022},
        {"car_name": "Magnite",
        "Manufacturer": "Nissan",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 4,
        "Baby": 2,
        "Year": 2022},
        {"car_name": "Punch",
        "Manufacturer": "Tata",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 5,
        "Baby": 4,
        "Year": 2021},
        {"car_name": "Seltos",
        "Manufacturer": "Kia",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 3,
        "Baby": 2,
        "Year": 2020},
        {"car_name": "Scorpio-N",
        "Manufacturer": "Mahindra",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 5,
        "Baby": 3,
        "Year": 2022},
         {"car_name": " S-Presso",
        "Manufacturer": "Maruti Suzuki",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 1,
        "Baby": 0,
        "Year": 2022},
        {"car_name": "Swift",
        "Manufacturer": "Maruti Suzuki",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 1,
        "Baby": 1,
        "Year": 2022},
         {"car_name": "Taigun",
        "Manufacturer": "Volkswagen",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 5,
        "Baby": 5,
        "Year": 2022},
        {"car_name": "Thar",
        "Manufacturer": "Mahindra",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 4,
        "Baby": 4,
        "Year": 2020},
        {"car_name": "Tigor",
        "Manufacturer": "Tata",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 4,
        "Baby": 3,
        "Year": 2020},
        {"car_name": "Tigor EV",
        "Manufacturer": "Tata",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 4,
        "Baby": 4,
        "Year": 2021},
         {"car_name": "Triber",
        "Manufacturer": "Renault",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 4,
        "Baby": 3,
        "Year": 2021},
        {"car_name": "Urban Cruiser",
        "Manufacturer": "Toyota",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 4,
        "Baby": 3,
        "Year": 2022},
        {"car_name": "XUV 300",
        "Manufacturer": "Mahindra",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 5,
        "Baby": 4,
        "Year": 2020},
        {"car_name": "XUV 700",
        "Manufacturer": "Mahindra",
        "NCAP": "Global NCAP",
        "Test": "2 Airbags",
        "Adult" : 5,
        "Baby": 4,
        "Year": 2021}
        ]
    }
    '''

    return data