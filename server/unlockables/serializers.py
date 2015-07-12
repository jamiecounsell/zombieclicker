from rest_framework import serializers
from .models import WeaponTool, ZombieTool, HealthTool

class WeaponSerializer(serializers.ModelSerializer):
	class Meta:
		model = WeaponTool

class ZombieSerializer(serializers.ModelSerializer):
	class Meta:
		model = ZombieTool

class HealthSerializer(serializers.ModelSerializer):
	class Meta:
		model = HealthTool