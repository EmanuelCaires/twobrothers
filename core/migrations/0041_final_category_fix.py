from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_final_category_fix'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            ALTER TABLE core_item 
            DROP COLUMN IF EXISTS category_id,
            DROP COLUMN IF EXISTS category;
            """,
            reverse_sql=""
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE core_item 
            ADD COLUMN category integer 
            REFERENCES core_category(id) 
            ON DELETE SET NULL;
            """,
            reverse_sql="ALTER TABLE core_item DROP COLUMN IF EXISTS category;"
        )
    ]
