
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from AppCrud.views import ListProductView,getData

urlpatterns = [
    path('',ListProductView.as_view(),name='home'),
    path('product/<int:id_product>/',getData,name='product'),
    path('ubah/<int:id_product>/',ListProductView.as_view(),name='ubah'),
    path('admin/', admin.site.urls),
]

