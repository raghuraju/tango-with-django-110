from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Page
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm


def add_page(request, category_slug_url):
	print category_slug_url
	try:
		category = Category.objects.filter(slug=category_slug_url)[0]
	except Category.DoesNotExist:
		category = None

	print category
	form = PageForm()
	if request.method == 'POST':
		form = PageForm(request.POST)
		if category:
			page = form.save(commit=False)
			page.category = category
			page.views = 0
			page.save()
			return show_category(request, category_slug_url)
		else:
			print form.errors
	_context = {
		'form': form, 
		'category': category,
		'title' : 'Add a Page'
	}
	return render(request, 'rango/add_page.html', context=_context)


def add_category(request):
	form = CategoryForm()

	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)

	return render(request, 'rango/add_category.html', {'form':form, 'title': 'Add a Category'})


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
	pages_list = Page.objects.order_by('-views')[:5]
	_context = {
		'categories': category_list,
		'most_viewed_pages': pages_list,
		'title' : 'Welcome to Tango with Django'
	}
	return render(request, 'rango/index.html', context=_context)


def about(request):
	_context = {"author": "Raghu"}
	return render(request, 'rango/about.html', context=_context)


def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit = False)
			profile.user = user
						
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True
		else:
			print user_form.errors
			print profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'rango/register.html', {
			'user_form': user_form,
			'profile_form': profile_form,
			'registered': registered
		})

