#!/usr/bin/env python
from __future__ import print_function

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django.settings.base')

import django
django.setup()

from rango.models import Category, Page

def populate():

	python_pages = [{
		'title': 'Python Homepage',
		'url': 'https://www.python.org/'
	},{
		'title': 'Python 2 Documentation',
		'url': 'https://docs.python.org/2/'
	},{
		'title': 'Python 3 Documentation',
		'url': 'https://docs.python.org/3/'
	},{
		'title': 'Learn Python the Hard Way - Book',
		'url': 'https://learnpythonthehardway.org/book/'
	}]

	django_pages = [{
		'title': 'Django Homepage',
		'url': 'https://www.djangoproject.com/'
	},{
		'title': 'Django Official Tutorial',
		'url': 'https://docs.djangoproject.com/en/1.10/intro/tutorial01/'
	},{
		'title': 'Tango with Django',
		'url': 'http://www.tangowithdjango.com/'
	},{
		'title': 'Django on Reddit',
		'url': 'https://www.reddit.com/r/django'
	}]

	other_pages = [{
		'title': 'Bottle: Python web framework',
		'url': 'http://bottlepy.org/docs/dev/index.html#'
	},{
		'title': 'Flask (A python microframework)',
		'url': 'http://flask.pocoo.org/'
	}]

	categories = {
		'Python': {'pages': python_pages},
		'Django': {'pages': django_pages},
		'Other Framework': {'pages': other_pages}
	}

	for cat, cat_data in categories.items():
		c = add_category(cat)
		for page in cat_data['pages']:
			add_page(c, page['title'], page['url'])

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))


def add_category(category_name):
	c = Category.objects.get_or_create(name=category_name)[0]
	c.save()

	return c

def add_page(category, title, url, views=0):
	p = Page.objects.get_or_create(category=category, title=title)
	p.url = url
	p.views = views
	p.save()

	return p


if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()