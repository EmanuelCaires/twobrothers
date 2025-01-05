from django.db import migrations

def copy_category_data(apps, schema_editor):
    Item = apps.get_model('core', 'Item')
    for item in Item.objects.all():
        if hasattr(item, 'category_0'):
            item.category = item.category_0
            item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_finalize_category_field'),
    ]

    operations = [
        migrations.RunPython(
            copy_category_data,
            reverse_code=migrations.RunPython.noop
        ),
    ]
