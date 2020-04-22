
from django.contrib.auth.models import User
from django.db import models
from PIL import Image

TAG_CHOICES = (
	('Other Electronics','Other Electronics'),
	('Laptops', 'Laptops'),
	('PC','PC'),
	('Tablets','Tablets'),
	('Mobiles','Mobiles'),
	('Clothes','Clothes'),
	('Automotives','Automotives'),
	('Furniture','Furniture'),
)


class Advert(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 20)
	product = models.CharField(max_length = 100)
	description = models.TextField(max_length= 2000)
	tags = models.CharField(max_length = 20, choices = TAG_CHOICES, default = "Undefined")
	date_posted = models.DateField(auto_now_add = True)
	price = models.PositiveIntegerField(default = 100)
	image = models.ImageField(upload_to = 'ad-photos')
	slug = models.SlugField(unique = True)
	sold = models.BooleanField(default = False)

	def __str__(self):
		return str(self.title)

class Notify(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user')
	buyer = models.ForeignKey(User, on_delete = models.CASCADE, related_name='buyer')
	product = models.ForeignKey(Advert, on_delete = models.CASCADE)
	date = models.DateField(auto_now_add = True)

	def __str__(self):
		return str(self.product)