from django.conf.urls.static import static
from django.urls import include, re_path
from django.urls import path
from ActualiteAPP import views
from ActualiteAPP.views import ActualiteList
from ccsmProject import settings

urlpatterns=[
    # re_path(r'^$',views.ActualiteList ),
    path('all', ActualiteList.as_view(), name="actualite-list")
]

