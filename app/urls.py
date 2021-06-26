from django.contrib import admin
from django.urls import path
from . import *
from MSSN.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = "index"),
    path('success', views.success, name = "success"),
    path('payment', views.payment, name = "payment"),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
