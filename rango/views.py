from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page


def show_category(request, category_name_url):
	_context = {}

	try:
		category = Category.objects.get(slug=category_name_url)
		pages = Page.objects.filter(category=category)
		_context['category'] = category
		_context['pages'] = pages
	except Category.DoesNotExist:
		_context['category'] = None
		_context['pages'] = None

	return render(request, 'rango/category.html', context=_context)


def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	_context = {'categories': category_list}
	return render(request, 'rango/index.html', context=_context)


def about(request):
	_context = {"author": "Raghu"}
	return render(request, 'rango/about.html', context=_context)