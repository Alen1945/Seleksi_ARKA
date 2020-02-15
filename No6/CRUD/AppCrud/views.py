from django.shortcuts import render
from django.views.generic import ListView,RedirectView
from .models import Product
# Create your views here.

class ListProductView(ListView):
	model=Product
	mode=None
	template_name='index.html'
	context_object_name='product'

	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(*args,**kwargs)
		return context

