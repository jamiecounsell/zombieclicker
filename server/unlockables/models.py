from django.db import models

class Unlockable(models.Model):
	name 		= models.CharField(max_length=50, blank=False, null=False)
	description = models.TextField(blank=False, null=False)
	cost		= models.IntegerField(blank=False, null=False)
	is_auto 	= models.BooleanField(default=True, null=False, blank=False)

	class Meta:
		abstract = True

	def getReadableName(self):
		return self.name

	def __unicode__(self):
		return self.getReadableName()

	def __str__(self):
		return self.getReadableName()

class WeaponTool(Unlockable):
	damage 		= models.IntegerField(blank=False, null=False)

class ZombieTool(Unlockable):
	zombies 	= models.IntegerField(blank=False, null=False)

class HealthTool(Unlockable):
	health 		= models.IntegerField(blank=False, null=False)