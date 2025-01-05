from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_fix_category_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
    ]
