
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from AppCrud.views import ListProductView

urlpatterns = [
    path('',ListProductView.as_view(),name='home'),
    path('admin/', admin.site.urls),
]

