from django import template

register = template.Library()

@register.inclusion_tag('some_template_name.html')
def nav_categorylist(depth, *args, **kwargs):
    # depth amount of navigation list items
    context = { depth : depth } # allows to set active and no link on last element
    for i in range(depth):
        try:
            name_key = "".format{}

            context[''] = kwargs['']

    # start with template!
    # TODO: build structure from as few arguments as possible

    return {'categories': categories}