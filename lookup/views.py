from django.shortcuts import render
import json
import requests
import urllib

# Create your views here.


def home(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		params = {
		'access_key': '31efc493add11887495530e3985d51b5',
		'type': 'Zipcode',
		'query': city
	}
		api_request = requests.get('http://api.weatherstack.com/current', params)


		try:
			api = api_request.json()
		except Exception as e:	
			api = "Error..."
		return render(request, 'home.html', {'api': api})

	else:
		url = 'http://ipinfo.io/json'
		response = urllib.request.urlopen(url)
		data = json.load(response)
		city = data['city']
		params = {
		'access_key': '31efc493add11887495530e3985d51b5',
		'query': city,
		'units': 'm'
	}
		api_request = requests.get('http://api.weatherstack.com/current', params)


		try:
			api = api_request.json()
		except Exception as e:	
			api = "Error..."
		return render(request, 'home.html', {'api': api})	
def about(request):
	return render(request, 'about.html')