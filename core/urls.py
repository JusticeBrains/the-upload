from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

admin.site.site_header = "We're Upload"
admin.site.site_title = " Upload Portal"
admin.site.index_title = "Welcome To Upload Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('document/', include('upload.urls', namespace='upload')),
    path('', include('pages.urls', namespace='pages')),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


