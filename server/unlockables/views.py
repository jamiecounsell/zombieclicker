from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import WeaponTool, ZombieTool, HealthTool
from .serializers import WeaponSerializer, ZombieSerializer, HealthSerializer

class WeaponList(generics.ListCreateAPIView):
	queryset = WeaponTool.objects.all()
	serializer_class = WeaponSerializer

class ZombieList(generics.ListCreateAPIView):
	queryset = ZombieTool.objects.all()
	serializer_class = ZombieSerializer

class HealthList(generics.ListCreateAPIView):
	queryset = HealthTool.objects.all()
	serializer_class = HealthSerializer
