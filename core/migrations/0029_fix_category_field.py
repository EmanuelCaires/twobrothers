from django.db import migrations, models

def update_model_state(apps, schema_editor):
    """Update the model state to recognize the existing ForeignKey"""
    Item = apps.get_model('core', 'Item')
    field = models.ForeignKey(
        'core.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Category',
        db_column='category_id'
    )
    field.contribute_to_class(Item, 'category')

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_make_category_nullable'),
    ]

    operations = [
        migrations.RunPython(
            update_model_state,
            reverse_code=migrations.RunPython.noop
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
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
