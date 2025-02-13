from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

class MediaStorage(FileSystemStorage):
    def __init__(self):
        super().__init__(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)

    def url(self, name):
        """
        Override url method to serve files through static in production
        """
        if not settings.DEBUG:
            # In production, serve through static
            return f"{settings.STATIC_URL}media/{name}"
        return super().url(name)

    def save(self, name, content, max_length=None):
        """
        Save the file and also copy it to static media directory in production
        """
        name = super().save(name, content, max_length)
        
        if not settings.DEBUG:
            # Copy to static media directory
            static_media_path = os.path.join(settings.STATIC_ROOT, 'media', name)
            os.makedirs(os.path.dirname(static_media_path), exist_ok=True)
            with open(static_media_path, 'wb') as static_file:
                for chunk in content.chunks():
                    static_file.write(chunk)
        
        return name
