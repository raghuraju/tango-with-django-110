from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_categories():
	return {'categories': Category.objects.all()}


@register.inclusion_tag('rango/categories.html')
def most_liked_categories():
	return {'categories': Category.objects.order_by('-likes')[:5], 'heading':'Most Liked Categories'}