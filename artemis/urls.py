from django.contrib import admin
from django.urls import path, include

# static files
from django.conf import settings
from django.conf.urls.static import static

# views
from django.views.generic.base import RedirectView
from . import views

from Collection.views import owners

favicon = RedirectView.as_view(url='/s/icons/favicon.ico', permanent=True)

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('favicon.ico', favicon),
    path('api/', include('Api.urls')),
    path('account/', include('Account.urls')),
    path('owners/<slug:username>', owners)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = views.error_400
handler403 = views.error_403
handler404 = views.error_404
handler500 = views.error_500