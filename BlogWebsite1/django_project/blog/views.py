from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author' : 'Abhineet',
		'title' : 'Blog Post 1',
		'content' : 'First blog content',
		'date_posted' : 'November 30'
	},
	{
		'author' : 'Deepak',
		'title' : 'Blog Post 2',
		'content' : 'Second blog content',
		'date_posted' : 'November 30'
	},
	{
		'author' : 'Navneet',
		'title' : 'Blog Post 3',
		'content' : 'Third blog content',
		'date_posted' : 'November 30'
	}
]

# 1)this functions handle traffic from home page
# we also need to map urlpattern to this function
# for this we create a urls.py file within this app
def home(request):
	context = {
		'posts' : posts
	}
	# return HttpResponse('<h1>Blog Home</h1>')
	return render(request, 'blog/home.html', context)

def about(request):
	# return HttpResponse('<h1>Blog About</h1>')
	return render(request, 'blog/about.html', {'title': 'About'})