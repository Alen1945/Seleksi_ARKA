from django.shortcuts import render,redirect
from django.views.generic import View,RedirectView
from .models import Product
from .forms import CreateProductForm
# Create your views here.

class ListProductView(View):
	template_name='index.html'
	product_form=CreateProductForm()
	context={}
	def get(self,*args,**kwargs):
		if kwargs.__contains__('id_product'):
			update_data=Product.objects.get(id=kwargs['id_product'])
			data=update_data.__dict__
			self.anggota_form=CreateProductForm(initial= data,instance=update_data)
			self.context['form']=self.product_form
			return self.context
		self.context['product']=Product.objects.all()
		self.context['forms']=self.product_form
		return render(self.request,self.template_name,self.context)	

	def post(self,*args,**kwargs):
		if kwargs.__contains__('id_product'):
			update_data=Product.objects.get(id=kwargs['id_product'])
			self.product_form=CreateProductForm(self.request.POST,instance=update_data)
		else:
			  self.anggota_form=CreateProductForm(self.request.POST)

		if self.anggota_form.is_valid():
			self.anggota_form.save()
		return redirect('home')


		
