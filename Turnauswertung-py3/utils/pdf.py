import os
from subprocess import Popen, PIPE
import tempfile

from django.http import HttpResponse
from django.template.loader import get_template


def create(template_location, context, file_name):
    template = get_template(template_location)
    rendered_tpl = template.render(context).encode('utf-8')
    print(rendered_tpl)

    with tempfile.TemporaryDirectory() as tempdir:
        # Create subprocess, supress output with PIPE and
        # run latex twice to generate the TOC properly.
        # Finally read the generated pdf.
        for i in range(2):
            process = Popen(
                ['pdflatex', '-output-directory', tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
            process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "filename={}".format(file_name)
    response.write(pdf)
    return response
