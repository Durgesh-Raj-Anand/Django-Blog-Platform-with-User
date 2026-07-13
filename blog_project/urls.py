"""
URL configuration for blog_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include blog app URLs at the root
    path('', include('blog.urls')),

    # Built-in auth views: /accounts/login/, /accounts/logout/, password reset, etc.
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
