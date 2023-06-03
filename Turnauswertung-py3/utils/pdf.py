import os
import tempfile
from subprocess import PIPE, Popen

from django.http import HttpResponse
from django.template.loader import get_template


def create(template_location, context, file_name):
    template = get_template(template_location)
    rendered_tpl = template.render(context).encode("utf-8")
    print(rendered_tpl)

    with tempfile.TemporaryDirectory() as tempdir:
        # Create subprocess, suppress output with PIPE and
        # run latex twice to generate the TOC properly.
        # Finally read the generated pdf.
        for i in range(2):
            process = Popen(
                ["/Library/TeX/texbin/pdflatex", "-output-directory", tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
            process.communicate(rendered_tpl)

        try:
            with open(os.path.join(tempdir, "texput.pdf"), "rb") as f:
                pdf = f.read()
        except FileNotFoundError:
            with open(os.path.join(tempdir, "texput.log"), "rb") as f:
                pdf = f.read()
            response = HttpResponse(content_type="application/txt")
            response["Content-Disposition"] = "filename={}".format(file_name + ".txt")
            response.write(pdf)
            return response

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "filename={}".format(file_name)
    response.write(pdf)
    return response
