from django.shortcuts import render
from django.contrib.auth.models import User, Group
from server.models import *
from api.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.decorators import detail_route, list_route


class CategorieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    serializer_class = CategorieSerializer
    queryset = Categorie.objects.all()

class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    @detail_route()
    def foods(self,request,pk=None):
        queryset = Food.objects.all().filter(restaurant=pk)
        serializer = FoodSerializer(queryset,many=True)
        return Response(serializer.data)

class FoodViewSet(viewsets.ReadOnlyModelViewSet):
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