from django.contrib.auth.models import User, Group
from rest_framework import serializers
from server.models import *
 
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'name', 'image', 'description','timestamp')

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'image', 'description','timestamp')

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name','description','categorie','image','cost','timestamp')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'table','foods','state','comment')