from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Check the columns of the core_item table'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name='core_item';")
            columns = cursor.fetchall()
            self.stdout.write("Columns in core_item table:")
            for column in columns:
                self.stdout.write(column[0])
