from django.shortcuts import render
import json
import requests

# Create your views here.


def home(request):
	params = {
	'access_key': '31efc493add11887495530e3985d51b5',
	'type': 'Zipcode',
	'query': 'Mehsana'
}
	api_request = requests.get('http://api.weatherstack.com/current', params)


	try:
		api = api_request.json()
	except Exception as e:	
		api = "Error..."
	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html')