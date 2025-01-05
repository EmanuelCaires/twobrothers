from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_final_category_fix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('P', 'Phones'), ('C', 'Cases'), ('RP', 'Replacement Parts')], max_length=20),
        ),
    ]
