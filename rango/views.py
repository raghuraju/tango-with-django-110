from registration.backends.simple.views import RegistrationView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Page
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm
from .utils import visitor_cookie_handler


class RangoRegistrationView(RegistrationView):
	def get_success_url(self, user):
		return '/rango/'


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
	request.session.set_test_cookie()
	category_list = Category.objects.order_by('-likes')[:5]
	pages_list = Page.objects.order_by('-views')[:5]
	_context = {
		'categories': category_list,
		'most_viewed_pages': pages_list,
		'title' : 'Welcome to Tango with Django'
	}

	response = render(request, 'rango/index.html', context=_context)
	visitor_cookie_handler(request, response)

	return response


def about(request):
	if request.session.test_cookie_worked():
		print "Test cookie worked!"
		request.session.delete_test_cookie()
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


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('rango:index'))
			else:
				return HttpResponse("Your account has been disabled. Please contact the admin.")
		else:
			return HttpResponse("Invalid username/password.")
	else:
		return render(request, 'rango/login.html', {})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('rango:index'))


@login_required
def restricted(request):
	return HttpResponse("Since you are logged in, you can see this message.")