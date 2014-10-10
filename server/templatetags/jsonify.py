from django import template
from django.utils.safestring import mark_safe
import json
from django.core import serializers

register = template.Library()

@register.filter('jsonify')
def jsonify(list):
	print list
	return mark_safe(serializers.serialize('json',list))