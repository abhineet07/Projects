from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# 1)this functions handle traffic from home page
# we also need to map urlpattern to this function
# for this we create a urls.py file within this app
def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	# return HttpResponse('<h1>Blog Home</h1>')
	return render(request, 'blog/home.html', context)

def about(request):
	# return HttpResponse('<h1>Blog About</h1>')
	return render(request, 'blog/about.html', {'title': 'About'})