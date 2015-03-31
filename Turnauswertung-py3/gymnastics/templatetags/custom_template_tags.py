from django import template
from django.utils.translation import ugettext_lazy

register = template.Library()

@register.inclusion_tag('templatetags/nav_item.html')
def render_nav_item(name, url_name='', url_id=None, active=False):
    return {'name': name, 'url_name': url_name, 'url_id': url_id, 'active': active}

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '')

@register.filter
def get_index(list_, index):
    return list_[int(index)]

@register.filter
def get_final_total(athlete, discipline):
    return athlete.final_total(discipline)

@register.filter
def translate(value):
    return ugettext_lazy(value)