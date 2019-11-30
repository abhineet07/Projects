from django.urls import path
from . import views

urlpatterns = [
	# the 'name' will be used for navigation from on page to another inside href
	# example : <a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a> 
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]