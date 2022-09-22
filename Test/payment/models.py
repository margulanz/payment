from django.db import models

# Create your models here.
class Item(models.Model):
	name		= models.CharField(max_length = 20)
	description = models.TextField()
	price		= models.IntegerField()


	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name


class Order(models.Model):
	item = models.ManyToManyField(Item, related_name = 'item')
	def __str__(self):
		return f"Order #{self.id}"
	def __repr__(self):
		return f"Order #{self.id}"