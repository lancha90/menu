from django.db import models

class OrderDTO(models.Model):
	id=models.AutoField(primary_key=True)
 
	def __init__(self,comment,order_id,table_name):
		self.id=1
		self.foods = []
		self.comment = comment
		self.order = order_id
		self.table = table_name
	
	def add_food(self, food,count):
		self.foods.append({'name':food,'count':count})