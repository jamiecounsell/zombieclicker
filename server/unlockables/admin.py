from django.contrib import admin
from .models import WeaponTool, ZombieTool, HealthTool

def getFieldList(fields):
	return ( 
			# Common fields on top
			'name',
			'cost'
		)+ fields + (
			# Common fields on bottom
			'description',
			'is_auto',
		)

class WeaponAdmin(admin.ModelAdmin):
	fields = getFieldList(('damage',))
	class Meta:
		model = WeaponTool
		

class ZombieAdmin(admin.ModelAdmin):
	fields = getFieldList(('zombies',))
	class Meta:
		model = ZombieTool
		

class HealthAdmin(admin.ModelAdmin):
	fields = getFieldList(('health',))
	class Meta:
		model = HealthTool

admin.site.register(WeaponTool, WeaponAdmin)
admin.site.register(ZombieTool, ZombieAdmin)
admin.site.register(HealthTool, HealthAdmin)
