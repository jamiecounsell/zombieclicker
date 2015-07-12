from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from jsonfield import JSONField

class SocialTokens(models.Model):
	fb = models.CharField(max_length=255, blank=True, null=True)
	gg = models.CharField(max_length=255, blank=True, null=True)
	tw = models.CharField(max_length=255, blank=True, null=True)
	def clean(self):
		if not ( self.fb and self.gg and self.tw ):
			raise ValidationError('At least one token is required')
		super(SocialTokens, self).clean()

class SaveState(models.Model):
	json = JSONField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):  
	user   = models.OneToOneField(User, null=False)
	name   = models.CharField( blank=True, null=True, max_length=50)
	email  = models.EmailField(blank=True, null=True)
	
	tokens = models.OneToOneField(SocialTokens, null=True, blank=True)

	save   = models.OneToOneField(SaveState, null=True, blank=True)

	def getReadableName(self):
		return self.name + ": " + self.email

	def __unicode__(self):
		return self.getReadableName()

	def __str__(self):
		return self.getReadableName()
