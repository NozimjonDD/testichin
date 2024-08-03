import pdfkit

from uuid import uuid4
from django.template.loader import get_template

from mininnovation_backend.settings import MEDIA_ROOT


def pdfmaker(content: str, upload_to: str):
    template = get_template('template.html')
    content = template.render({
        'content': content
    })
    options = {
        'page-size': 'A4',
        'margin-top': '0.55in',
        'margin-right': '0.55in',
        'margin-bottom': '0.55in',
        'margin-left': '0.55in',
        'encoding': "UTF-8",
    }
    filename = '{}{}.{}'.format(upload_to, uuid4().hex, 'pdf')  # set filename as random string
    upload_to = MEDIA_ROOT + f'/{filename}'
    if pdfkit.from_string(content, upload_to, options=options):
        return filename
