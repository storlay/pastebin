from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('text.urls')),
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),

    path('social-auth/', include(('social_django.urls', 'social'), namespace='social'))
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
