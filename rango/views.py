from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse('Hey there! How are you? <a href="/rango/about/">About</a>')

def about(request):
	return HttpResponse('Rango says here is the about page. <a href="/rango/">Home</a>')