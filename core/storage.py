from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import shutil

class MediaStorage(FileSystemStorage):
    def __init__(self):
        super().__init__(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)

    def url(self, name):
        """
        Override url method to serve files through static in production
        """
        if not settings.DEBUG:
            # In production, serve through static/media
            return f"/static/media/{name}"
        return super().url(name)

    def save(self, name, content, max_length=None):
        """
        Save the file and also copy it to staticfiles/media directory in production
        """
        name = super().save(name, content, max_length)
        
        if not settings.DEBUG:
            # Copy to staticfiles/media directory
            static_media_path = os.path.join(settings.STATIC_ROOT, 'media', name)
            os.makedirs(os.path.dirname(static_media_path), exist_ok=True)
            
            # Ensure content is at the start
            if hasattr(content, 'seek'):
                content.seek(0)
            
            # Copy the file
            with open(static_media_path, 'wb') as static_file:
                if hasattr(content, 'chunks'):
                    for chunk in content.chunks():
                        static_file.write(chunk)
                else:
                    shutil.copyfile(os.path.join(settings.MEDIA_ROOT, name), static_media_path)
        
        return name
