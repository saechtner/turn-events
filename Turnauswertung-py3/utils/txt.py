from django.http import HttpResponse
from django.template.loader import get_template


def create(template_location, context, file_name):
    template = get_template(template_location)
    txt = template.render(context).encode("utf-8")

    response = HttpResponse(content_type="application/txt")
    response["Content-Disposition"] = "filename={}".format(file_name)
    response.write(txt)
    return response
