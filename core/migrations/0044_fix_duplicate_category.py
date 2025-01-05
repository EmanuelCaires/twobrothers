from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_fix_category_length'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            ALTER TABLE core_item 
            DROP COLUMN IF EXISTS category_id;
            """,
            reverse_sql=""
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE core_item 
            ADD COLUMN category_id integer 
            REFERENCES core_category(id) 
            ON DELETE SET NULL;
            """,
            reverse_sql="ALTER TABLE core_item DROP COLUMN IF EXISTS category_id;"
        )
    ]
