from django.db import migrations
from django.conf import settings

def update_site_domain(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    site = Site.objects.get(id=settings.SITE_ID)
    site.domain = '127.0.0.1:8080'
    site.name = 'WeRepair Development'
    site.save()

def revert_site_domain(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    site = Site.objects.get(id=settings.SITE_ID)
    site.domain = 'example.com'
    site.name = 'example.com'
    site.save()

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(update_site_domain, revert_site_domain),
    ]
