from pathlib import Path
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string  # Import render_to_string
from django.utils.html import strip_tags

def sendMail(emails, template, subject="Inscription à notre Newsletter",context = {}):
    """
    Envoyez des emails a un ou plusieurs utilisateurs (hosts)
    """

    # Render the HTML content using the context


    # Use render_to_string to render the HTML content from the template
    email_content = render_to_string(template, context)
    plain_message = strip_tags(email_content)
    # Create an EmailMessage object and send it
    send_mail(subject, plain_message,recipient_list=emails,from_email="contact@workinmusic.fr", html_message=email_content)

