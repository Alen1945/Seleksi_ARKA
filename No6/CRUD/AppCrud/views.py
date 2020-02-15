from django.shortcuts import render,redirect
from django.views.generic import View,RedirectView
from .models import Product
from .forms import CreateProductForm
from django.http import JsonResponse
# Create your views here.

class ListProductView(View):
	template_name='index.html'
	product_form=CreateProductForm()
	context={}
	def get(self,*args,**kwargs):
		self.context['product']=Product.objects.all()
		self.context['forms']=self.product_form
		return render(self.request,self.template_name,self.context)	

	def post(self,*args,**kwargs):
		if kwargs.__contains__('id_product'):
			update_data=Product.objects.get(id=kwargs['id_product'])
			self.product_form=CreateProductForm(self.request.POST,instance=update_data)
		else:
			  self.product_form=CreateProductForm(self.request.POST)

		if self.product_form.is_valid():
			self.product_form.save()
		return redirect('home')


def getData(request,**kwargs):
	product_form=CreateProductForm()
	context={}
	if kwargs.__contains__('id_product'):
		update_data=Product.objects.get(id=kwargs['id_product'])
		data=update_data.__dict__
		product_form=CreateProductForm(initial= data,instance=update_data)
		context['form']=product_form
		return render(request,'formEdit.html',context)
	else:
		return False
		

