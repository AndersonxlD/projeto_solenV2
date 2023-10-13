from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from app_solen import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_solen.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error404
handler500 = views.error500