import os

from dotenv import load_dotenv
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

load_dotenv()


def send_mail(email, key):
    html_content = f'<h2>Ваша заявка принята. Ключевые слова для проверки результата заявки: {key}</h2><br>' \
                   f"<h2>Sizning murojaatingiz qabul qilindi. Murojaat natijasini tekshirish uchun kalit so'z: {key}</h2>"
    plain_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject='That’s your subject',
        body=plain_content,
        from_email=os.getenv('EMAIL_HOST'),
        to=[email],
    )
    email.attach_alternative(html_content, 'text/html')
    return email.send()
