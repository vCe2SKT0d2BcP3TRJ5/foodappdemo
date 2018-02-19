from django.db import models

class Category(models.Model):
	class Meta:
		verbose_name_plural = "categories"
	category = models.CharField(max_length=255, unique=True)

	def __str__(self):
		return self.category


class Item(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	item = models.CharField(max_length=255, unique=True)

	def __str__(self):
		return self.item