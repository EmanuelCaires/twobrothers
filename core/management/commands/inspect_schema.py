from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Inspect database schema for core_item table'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Check column nullability
            cursor.execute("""
                SELECT column_name, is_nullable 
                FROM information_schema.columns 
                WHERE table_name = 'core_item'
            """)
            results = cursor.fetchall()
            
            self.stdout.write("core_item table columns:")
            for column, nullable in results:
                self.stdout.write(f"{column}: {'NULL' if nullable == 'YES' else 'NOT NULL'}")

            # Check constraints
            cursor.execute("""
                SELECT conname, pg_get_constraintdef(c.oid)
                FROM pg_constraint c
                JOIN pg_class t ON c.conrelid = t.oid
                WHERE t.relname = 'core_item'
            """)
            constraints = cursor.fetchall()
            
            self.stdout.write("\ncore_item table constraints:")
            for name, definition in constraints:
                self.stdout.write(f"{name}: {definition}")

            # Check triggers
            cursor.execute("""
                SELECT tgname, pg_get_triggerdef(oid)
                FROM pg_trigger
                WHERE tgrelid = 'core_item'::regclass
            """)
            triggers = cursor.fetchall()
            
            self.stdout.write("\ncore_item table triggers:")
            for name, definition in triggers:
                self.stdout.write(f"{name}: {definition}")
