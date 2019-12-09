from django.http import HttpResponse

def youtube(request):
	return HttpResponse('''<a href="https://www.youtube.com/"> youtube </a>''')

def hackerrank(request):
	return HttpResponse('''<a href="https://www.hackerrank.com/dashboard"> hackerrank </a>''')

def chegg(request):
	return HttpResponse('''<a href="https://www.chegg.com/my/expertqa"> chegg </a>''')

def codechef(request):
	return HttpResponse('''<a href="https://www.codechef.com/"> codechef </a>''')

def hackerearth(request):
	return HttpResponse('''<a href="https://www.hackerearth.com/challenges/"> hackerearth </a>''')