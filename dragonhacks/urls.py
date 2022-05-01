from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('accounts/', include('accounts.urls')),
    path('gym/', include('gym.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
