from django.db import migrations
from django.utils.text import slugify

def populate_slugs(apps, schema_editor):
    Item = apps.get_model('core', 'Item')
    for item in Item.objects.all():
        item.slug = slugify(item.name)
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_add_category_id_to_item'),
    ]

    operations = [
        migrations.RunPython(populate_slugs),
    ]
