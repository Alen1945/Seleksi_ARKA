from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=('cashier','name','category','price')
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		for f in self.fields.values():
			f.widget.attrs={'class':'form-control'}