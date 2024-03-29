from django.db import models
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    site_name 		 = models.CharField(max_length=255, default='Zombie Clicker')

    def __unicode__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"

