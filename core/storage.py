from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

class MediaStorage(FileSystemStorage):
    def __init__(self):
        location = settings.MEDIA_ROOT if settings.DEBUG else os.path.join(settings.STATIC_ROOT, 'media')
        base_url = settings.MEDIA_URL if settings.DEBUG else f"{settings.STATIC_URL}media/"
        super().__init__(location=location, base_url=base_url)

    def _save(self, name, content):
        """
        Save the file to the appropriate location
        """
        # Clean the file name to prevent any path traversal
        name = self.get_valid_name(self.get_available_name(name))
        
        # Save the file
        name = super()._save(name, content)
        
        # In production, ensure the file exists in both media_root and static/media
        if not settings.DEBUG:
            media_path = os.path.join(settings.MEDIA_ROOT, name)
            static_path = os.path.join(settings.STATIC_ROOT, 'media', name)
            
            # Create directories if they don't exist
            os.makedirs(os.path.dirname(media_path), exist_ok=True)
            os.makedirs(os.path.dirname(static_path), exist_ok=True)
            
            # Copy to both locations
            if not os.path.exists(media_path):
                shutil.copy2(os.path.join(self.location, name), media_path)
            if not os.path.exists(static_path):
                shutil.copy2(os.path.join(self.location, name), static_path)
        
        return name

    def url(self, name):
        """
        Return the URL where the file can be accessed
        """
        if settings.DEBUG:
            return super().url(name)
        else:
            # In production, serve through the static URL
            return f"{settings.STATIC_URL}media/{name}"
