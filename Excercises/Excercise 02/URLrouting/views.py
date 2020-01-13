from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# return HttpResponse("Home ")
	return render(request, 'index.html')

def removepunc(request):
	djtext = request.GET.get('text', 'default')
	print(djtext)
	return HttpResponse('''remove punc <a href="/"> Go Back </a>''')

def capfirst(request):
	return HttpResponse('''capitalize first <a href="/"> Go Back </a>''')

def newlineremove(request):
	return HttpResponse('''remove new line <a href="/"> Go Back </a>''')

def spaceremove(request):
	return HttpResponse('''remove space <a href="/"> Go Back </a>''')

def charcount(request):
	return  HttpResponse('''char count <a href="/"> Go Back </a>''')