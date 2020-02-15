
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from AppCrud.views import ListProductView

urlpatterns = [
    path('',ListProductView.as_view(),name='home'),
    path('get/<int:id_anggota>/',ListProductView.as_view(),name='ubah'),
    path('ubah/<int:id_anggota>/',ListProductView.as_view(),name='ubah'),
    path('admin/', admin.site.urls),
]

