from django.db import models

# Create your models here.
class Categorie(models.Model):
	id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	icon=models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)