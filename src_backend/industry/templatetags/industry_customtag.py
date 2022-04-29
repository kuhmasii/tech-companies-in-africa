from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def seperate_string(value):
	"""
	Seperating the sentence of the value based on
	 ',' and turning it into a normal python list.
	"""
	value = [x.strip() for x in value.split(",")]
	return value
