from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.models import Categorie
from api.serializers import UserSerializer, GroupSerializer, CategorieSerializer
from rest_framework import viewsets
from rest_framework.permissions import *

class CategorieViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows categories to be viewed or edited.
    """
	serializer_class = CategorieSerializer
	queryset = Categorie.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer