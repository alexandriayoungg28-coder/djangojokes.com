from django.core.mail import EmailMessage


def send_email(to, subject, content):
    email = EmailMessage(
        subject=subject,
        body=content,
        to=[to],
    )
    email.content_subtype = 'html'
    return email.send()