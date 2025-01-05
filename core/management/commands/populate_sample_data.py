from django.core.management.base import BaseCommand
from core.models import Item, Category
import os

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        # Create categories
        phones_category = Category.objects.create(
            title='Phones',
            category='P',
            label='P',
            description='Smartphones and mobile devices',
            slug='phones',
            price=0,
            discount_price=None
        )
        cases_category = Category.objects.create(
            title='Cases',
            category='C',
            label='S',
            description='Phone cases and covers',
            slug='cases',
            price=0,
            discount_price=None
        )
        parts_category = Category.objects.create(
            title='Replacement Parts',
            category='RP',
            label='D',
            description='Replacement parts for phones',
            slug='replacement-parts',
            price=0,
            discount_price=None
        )

        # Create sample items
        Item.objects.create(
            name='iPhone 15',
            price=999.99,
            description='Latest iPhone model',
            image='iphone15.png',
            category=phones_category
        )

        Item.objects.create(
            name='iPhone SE',
            price=399.99,
            description='Compact iPhone model',
            image='iphonese.png',
            category=phones_category
        )

        Item.objects.create(
            name='Honor Magic',
            price=799.99,
            description='Premium Android phone',
            image='Honor_Magic.png',
            category=phones_category
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated sample data'))
