import sendgrid
from sendgrid.helpers.mail import Email, To, Content, Mail
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend

class SendGridBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently)
        self.sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        self.from_email = settings.DEFAULT_FROM_EMAIL

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        num_sent = 0
        for message in email_messages:
            try:
                from_email = Email(message.from_email or self.from_email)
                for to_email in message.to:
                    to_email = To(to_email)
                    content = Content("text/plain", message.body)
                    mail = Mail(from_email, to_email, message.subject, content)
                    
                    # Add HTML content if present
                    if message.alternatives and len(message.alternatives) > 0:
                        html_content = message.alternatives[0][0]
                        if message.alternatives[0][1] == 'text/html':
                            mail.add_content(Content("text/html", html_content))

                    self.sg.client.mail.send.post(request_body=mail.get())
                    num_sent += 1
            except Exception as e:
                if not self.fail_silently:
                    raise e
        return num_sent
