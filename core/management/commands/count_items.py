from django.core.management.base import BaseCommand
from core.models import Item

class Command(BaseCommand):
    help = 'Count the number of items in the Item table'

    def handle(self, *args, **kwargs):
        item_count = Item.objects.count()
        self.stdout.write(f'Total items: {item_count}')
