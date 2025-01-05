from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_safe_category_fix'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1 
                    FROM information_schema.columns 
                    WHERE table_name='core_item' 
                    AND column_name='category_id'
                ) THEN
                    ALTER TABLE core_item 
                    DROP COLUMN category_id;
                END IF;
            END $$;
            """,
            reverse_sql=""
        ),
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 
                    FROM information_schema.columns 
                    WHERE table_name='core_item' 
                    AND column_name='category'
                ) THEN
                    ALTER TABLE core_item 
                    ADD COLUMN category integer 
                    REFERENCES core_category(id) 
                    ON DELETE SET NULL;
                END IF;
            END $$;
            """,
            reverse_sql="ALTER TABLE core_item DROP COLUMN IF EXISTS category;"
        )
    ]
