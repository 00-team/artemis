from django.contrib import admin
from django.urls import path, include

# static files
from django.conf import settings
from django.conf.urls.static import static

# views
from django.views.generic.base import RedirectView

favicon = RedirectView.as_view(url='/s/icons/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', favicon),
    path('api/', include('Api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error Pages
from . import views

handler400 = views.error_400
handler403 = views.error_403
handler404 = views.error_404
handler500 = views.error_500