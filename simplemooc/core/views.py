from django.shortcuts import render
from django.http import HttpResponse #Sempre tem que existe para chamada de view em django
			

def home(request):
	return render(request, 'home.html')

def contact(request):
	return render(request, 'contact.html')