from django.db import migrations, models

def migrate_data(apps, schema_editor):
    Item = apps.get_model('core', 'Item')
    for item in Item.objects.all():
        # If there's any old category data, migrate it
        if hasattr(item, 'category') and item.category:
            # Create or find the corresponding Category
            Category = apps.get_model('core', 'Category')
            category, _ = Category.objects.get_or_create(
                category=item.category,
                defaults={
                    'title': item.category,
                    'description': 'Migrated category',
                    'slug': item.category.lower()
                }
            )
            item.category_fk = category
            item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_fix_category_data'),
    ]

    operations = [
        # Add new ForeignKey field only if it doesn't exist
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 
                    FROM information_schema.columns 
                    WHERE table_name='core_item' 
                    AND column_name='category_id'
                ) THEN
                    ALTER TABLE core_item 
                    ADD COLUMN category_id integer 
                    REFERENCES core_category(id) 
                    ON DELETE SET NULL;
                END IF;
            END $$;
            """,
            reverse_sql="ALTER TABLE core_item DROP COLUMN IF EXISTS category_id;"
        ),
        # Migrate data
        migrations.RunPython(
            migrate_data,
            reverse_code=migrations.RunPython.noop
        ),
        # Remove old category field if it exists
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1 
                    FROM information_schema.columns 
                    WHERE table_name='core_item' 
                    AND column_name='category'
                ) THEN
                    ALTER TABLE core_item 
                    DROP COLUMN category;
                END IF;
            END $$;
            """,
            reverse_sql="ALTER TABLE core_item ADD COLUMN category varchar(2);"
        ),
        # Rename new field to category
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
                    RENAME COLUMN category_id TO category;
                END IF;
            END $$;
            """,
            reverse_sql="ALTER TABLE core_item RENAME COLUMN category TO category_id;"
        ),
    ]
