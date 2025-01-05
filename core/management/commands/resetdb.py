from django.core.management.base import BaseCommand
from django.db import connection
import psycopg2

class Command(BaseCommand):
    help = 'Drops and recreates the database'

    def handle(self, *args, **options):
        db_settings = connection.settings_dict
        db_name = db_settings['NAME']
        
        # Connect to postgres database to drop the target database
        conn = psycopg2.connect(
            dbname='postgres',
            user=db_settings['USER'],
            password=db_settings['PASSWORD'],
            host=db_settings['HOST'],
            port=db_settings['PORT']
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Terminate all connections to the target database
        cursor.execute(f"""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = '{db_name}'
              AND pid <> pg_backend_pid();
        """)
        
        # Drop and recreate the database
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cursor.execute(f"CREATE DATABASE {db_name}")
        
        cursor.close()
        conn.close()
        
        self.stdout.write(self.style.SUCCESS(f'Successfully reset database {db_name}'))
