from django.core.management.base import BaseCommand
from django.conf import settings
import os
import shutil

class Command(BaseCommand):
    help = 'Collects media files into the static directory for production serving'

    def handle(self, *args, **options):
        media_static = os.path.join(settings.STATIC_ROOT, 'media')
        
        # Ensure the static media directory exists
        if not os.path.exists(media_static):
            os.makedirs(media_static)
            self.stdout.write('Created static media directory')
            
        # Copy media files if they exist
        if os.path.exists(settings.MEDIA_ROOT):
            self.stdout.write('Copying media files to static directory...')
            
            # Walk through all files in MEDIA_ROOT
            for root, dirs, files in os.walk(settings.MEDIA_ROOT):
                for file in files:
                    # Get the source and destination paths
                    src = os.path.join(root, file)
                    rel_path = os.path.relpath(src, settings.MEDIA_ROOT)
                    dst = os.path.join(media_static, rel_path)
                    
                    # Create destination directory if it doesn't exist
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    
                    try:
                        # Copy the file with metadata
                        shutil.copy2(src, dst)
                        self.stdout.write(f'Successfully copied {rel_path}')
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f'Error copying {rel_path}: {str(e)}')
                        )
            
            self.stdout.write(
                self.style.SUCCESS('Successfully collected all media files')
            )
        else:
            self.stdout.write(
                self.style.WARNING('No media files found in MEDIA_ROOT')
            )
