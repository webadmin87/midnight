from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_templated_mail(tpl, subject, context, to=getattr(settings, 'MIDNIGHT_MAIN_ADMIN_EMAIL', 'admin@example.com')):

    msg_html = render_to_string(tpl, {'context': context})

    send_mail(subject, '', getattr(settings, 'MIDNIGHT_MAIN_MAIL_FROM', 'admin@example.com'),  [to], html_message=msg_html,)

