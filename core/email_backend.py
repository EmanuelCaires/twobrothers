import sys
from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend

class DebugEmailBackend(ConsoleEmailBackend):
    def send_messages(self, email_messages):
        for message in email_messages:
            print('\n' + '=' * 80)
            print('DEBUG EMAIL')
            print('=' * 80)
            print(f'From: {message.from_email}')
            print(f'To: {message.to}')
            print(f'Subject: {message.subject}')
            print('-' * 80)
            print('Body:')
            print(message.body)
            print('=' * 80 + '\n')
            sys.stdout.flush()
        return super().send_messages(email_messages)
