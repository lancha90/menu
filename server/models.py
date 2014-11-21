#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db import models
import datetime

ORDER_STATE =(
	(0, 'Cerrada'),
    (1, 'Pendiente'),
    (2, 'Cancelada'),
)

# Create your models here.

class Image(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	url=models.FileField(upload_to='weeat', verbose_name='Imagen')
	def __unicode__(self):
		return u'%s' % (self.url)
	def natural_key(self):
		return u'%s' % (self.url)

class Country(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	prefix=models.IntegerField()
	timestamp=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)
	def natural_key(self):
		return u'%s  - %s' % (self.id,self.name)

class City(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	prefix=models.IntegerField()
	country=models.ForeignKey(Country, related_name='u+')
	zip=models.CharField(max_length=10)
	timestamp=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)
	def natural_key(self):
		return u'%s  - %s' % (self.id,self.name)

class Categorie(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	image=models.FileField(upload_to='weeat', verbose_name='Imagen')
	description=models.CharField(max_length=1000)
	timestamp=models.DateTimeField(auto_now_add=True)
	index = models.IntegerField()
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)
	def natural_key(self):
		return u'%s  - %s' % (self.id,self.name)
	class Meta:
		ordering = ('index',)

class Restaurant(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	email=models.EmailField()
	address=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	image=models.FileField(upload_to='weeat', verbose_name='Imagen')
	description=models.CharField(max_length=1000)
	user=models.ForeignKey(User, related_name='u+')
	city=models.ForeignKey(City, related_name='u+')
	latitud=models.DecimalField(max_digits=13, decimal_places=10)
	longitud=models.DecimalField(max_digits=13, decimal_places=10)
	timestamp=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)
	def natural_key(self):
		return u'%s  - %s' % (self.id,self.name)

class Food(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	restaurant=models.ForeignKey(Restaurant, related_name='u+')
	categorie=models.ManyToManyField(Categorie, related_name='Categories')
	cost=models.DecimalField(max_digits=20, decimal_places=0)
	description=models.CharField(max_length=1000)
	image=models.ManyToManyField(Image, related_name='Images')
	timestamp=models.DateTimeField(auto_now_add=True)
	index = models.IntegerField()
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)
	def natural_key(self):
		return u'%s  - %s' % (self.id,self.name)
	class Meta:
		ordering = ('index',)

class Table(models.Model):
	id=models.AutoField(primary_key=True)
	number=models.IntegerField()
	restaurant=models.ForeignKey(Restaurant, related_name='u+')
	timestamp=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.restaurant)
	def natural_key(self):
		return u'%s  - %s' % (self.id,self.restaurant)


class Order(models.Model):
	id=models.AutoField(primary_key=True)
	table=models.ForeignKey(Table, related_name='u+')
	foods=models.ManyToManyField(Food, related_name='u+', through='Details')
	comment=models.CharField(max_length=1000)
	state=models.IntegerField(choices=ORDER_STATE,max_length=2)
	def __unicode__(self):
		return u'table: %s  Restaurant: %s Foods: %s' % (self.table.id,self.table.restaurant,self.foods.count())
	def natural_key(self):
		return u'table: %s  Restaurant: %s Foods: %s' % (self.table.id,self.table.restaurant,self.foods.count())

class Details(models.Model):
	order=models.ForeignKey(Order, related_name='u+')
	food=models.ForeignKey(Food, related_name='u+')
	count=models.IntegerField()
	timestamp=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'order: %s  -  Food: %s' % (self.order.id,self.food.name)
	def natural_key(self):
		return u'order: %s  -  Food: %s' % (self.order.id,self.food.name)