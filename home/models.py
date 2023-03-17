from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 300)
	slug = models.CharField(max_length = 500,unique = True)
	icon = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length = 300)
	slug = models.CharField(max_length = 500,unique = True)
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	def __str__(self):
		return self.name

class Slider(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField(null = True)
	description = models.TextField(blank = True)
	url = models.URLField(max_length = 500)
	def __str__(self):
		return self.name

class Brand(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	slug = models.CharField(max_length = 500,unique = True)
	def __str__(self):
		return self.name

class Ad(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	description = models.TextField(blank = True)
	rank = models.IntegerField(null = True)
	def __str__(self):
		return self.name

STOCK = (('in','In Stock'),('out','Out of Stock'))
LABELS = (('new','new'),('hot','hot'),('sale','sale'),('','default'))
class Product(models.Model):
	name = models.CharField(max_length = 300)
	slug = models.CharField(max_length = 500,unique = True)
	price = models.IntegerField()
	discounted_price = models.IntegerField()
	image = models.ImageField(upload_to = 'media')
	description = RichTextField(blank = True)
	specification = RichTextField(blank = True)
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	subcategory = models.ForeignKey(SubCategory,on_delete = models.CASCADE)
	brand = models.ForeignKey(Brand,on_delete = models.CASCADE, blank =True, null = True)
	stock = models.CharField(choices = STOCK,max_length = 100)
	labels = models.CharField(choices = LABELS,blank = True,max_length=100)

	def __str__(self):
		return self.name


class Customer(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	post = models.CharField(max_length = 400)
	description = models.TextField()

	def __str__(self):
		return self.name

class Cart(models.Model):
	username = models.CharField(max_length = 300)
	slug = models.CharField(max_length = 300, unique = True)
	items = models.ForeignKey(Product,on_delete = models.CASCADE)
	checkout = models.BooleanField(default = False)
	quantity = models.IntegerField(default = 1)
	total = models.DecimalField(max_digits=15, decimal_places=2, default=0)	
	def __str__(self):
		return self.username


class ProductReview(models.Model):
	slug = models.CharField(max_length= 400)
	username = models.CharField(max_length= 300)
	email = models.EmailField(max_length= 200)
	star = models.IntegerField(default = 1)
	review = models.TextField()

	def __str__(self):
		return self.username


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.TextField(blank = True)
    messege = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
    	return self.name
	