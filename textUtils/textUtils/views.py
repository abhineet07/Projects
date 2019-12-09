# I have created this file - Abhineet
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Hello Man!!</h1>")

def about(request):
	return HttpResponse("About me ??")