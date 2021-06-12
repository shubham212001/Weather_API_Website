""" Views are Python functions which take a URL request as parameter 
    and return an HTTP response or throw an exception like 404."""

from django.shortcuts import redirect, render

# Create your views here.


'''Importing urllib.request module . This is URL handling module i.e fetching URLs  '''
import urllib.request

# Importing json module to work with JSON data.
import json


#Defining index function which takes request as a parameter 
def index(request):
    if request.method=='POST':
        city=request.POST['city']

        #Source variable stores all json data from the API.
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=d8d31293bee740761c9ba933823c09ea').read()

        
        list_of_data = json.loads(source)

        #Creating a dictionary which stores the data to be rendered on html page.
        data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', '
                + str(list_of_data['coord']['lat']),

                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }
        print(data)
    
    else:
         data = {}
        

    return render(request, "main/index.html", data)