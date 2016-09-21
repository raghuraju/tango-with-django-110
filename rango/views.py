from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	_context = {'boldMessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context=_context)

def about(request):
	_context = {"author": "Raghu"}
	return render(request, 'rango/about.html', context=_context)