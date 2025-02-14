from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

class MediaStorage(FileSystemStorage):
    def __init__(self):
        super().__init__(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)

    def url(self, name):
        """
        Return URL for accessing the media file
        """
        url = super().url(name)
        if not settings.DEBUG:
            # In production, ensure media files are served from the correct path
            url = f"{settings.STATIC_URL}media/{name}"
        return url

    def _save(self, name, content):
        """
        Save the file and copy it to static/media in production
        """
        # Save to media directory
        name = super()._save(name, content)
        
        if not settings.DEBUG:
            # Also save to static/media for production
            static_path = os.path.join(settings.STATIC_ROOT, 'media', name)
            os.makedirs(os.path.dirname(static_path), exist_ok=True)
            
            # Copy the file
            with open(os.path.join(settings.MEDIA_ROOT, name), 'rb') as source:
                with open(static_path, 'wb') as dest:
                    dest.write(source.read())
        
        return name
