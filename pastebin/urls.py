from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('text.urls')),
    path('ps-admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),

    path('social-auth/', include(('social_django.urls', 'social'), namespace='social'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]

admin.site.site_header = 'Administration panel'
admin.site.index_title = '✉️ Pastebin'

handler404 = 'text.views.page_not_found_view'
