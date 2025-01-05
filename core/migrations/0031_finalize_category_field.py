from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_cleanup_category_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(
                to='core.Category',
                on_delete=models.SET_NULL,
                null=True,
                blank=True,
                verbose_name='Category',
                db_column='category_id'
            ),
        ),
    ]
