import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
]

# Debug toolbar for development
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    # In debug mode, serve media files directly
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Always serve media files, regardless of DEBUG setting
urlpatterns += [
    path('media/<path:path>', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
