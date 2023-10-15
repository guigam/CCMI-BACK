
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^actualite/',include('ActualiteAPP.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
