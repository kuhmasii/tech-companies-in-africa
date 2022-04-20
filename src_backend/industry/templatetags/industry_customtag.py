from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def seperate_string(value, arg):
	"""
	Seperate the sentence of a value, seperating it based on
	 ',' and bringing each value out provided by the index to 
	 the corresponding value.
	"""
	value = [x.strip() for x in value.split(",")]
	try:
		num = int(arg)
	except:
		raise ValueError ('The args should be an instance of a number.')


	if len(value) == 1:
		return value[-1]
	
	elif len(value) > 1:
		if num == 1:
			num = 0
		else:
			num -= 1
		if not IndexError:
			return value[num]


