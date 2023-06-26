from django.core.mail import send_mail
from django.conf import settings


def send_email(email):
    subject = "This email is from Django server"
    message = "This message is from Django server blablabla"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)