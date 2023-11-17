from django.conf import settings
from django.core.mail import send_mail
def send_email_to_client(email):
    subject = "Hazem email sender"
    message = "Hello my freind  iam hazem django dev it is message from me to have anice day "
    from_email =settings.EMAIL_HOST_USER
    to_list = [email]
    send_mail(subject ,message,from_email , to_list)