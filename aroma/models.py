from django.db import models

# Create your models here.

class Product(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 64)
	image = models.CharField(max_length = 128)
	category = models.CharField(max_length = 128)
	price = models.PositiveIntegerField()
	
	def __str__(self):
		return f'Товар: {self.name} - id товара: {self.id}'