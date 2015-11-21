from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_templated_mail(tpl, subject, context, to=settings.ADMIN_EMAIL):

    msg_html = render_to_string(tpl, {'context': context})

    send_mail(subject, '', settings.MAIL_FROM,  [to], html_message=msg_html,)

