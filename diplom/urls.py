from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/', include('core.urls')),
    path('', TemplateView.as_view(template_name="application.html"), name="app"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)