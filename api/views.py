from django.shortcuts import render
from django.contrib.auth.models import User, Group
from server.models import *
from api.serializers import *
from rest_framework import viewsets
from rest_framework.permissions import *

class CategorieViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows categories to be viewed or edited.
    """
	serializer_class = CategorieSerializer
	queryset = Categorie.objects.all()

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #permission_classes = (IsAdminUser,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer