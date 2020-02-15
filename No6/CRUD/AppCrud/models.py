from django.db import models

# Create your models here.

status_choice=(
		(0,'Survey'),
		(1,'Anggota Baru'),
	)
class Category(models.Model):
	nama=models.CharField(max_length=255)
	def __str__(self):
		return self.nama

class Cashier(models.Model):
	nama=models.CharField(max_length=255)
	def __str__(self):
		return self.nama

class Product(models.Model):
	id_category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
	id_cashier = models.ForeignKey(Cashier, on_delete=models.DO_NOTHING)
	nama=models.CharField(max_length=255)
	price=models.DecimalField(max_digits=10,decimal_places=2)

	def __str__(self):
		return self.nama
