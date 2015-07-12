from django.contrib import admin
from solo.admin import SingletonModelAdmin
from config.models import SiteConfiguration
from django.db.utils import OperationalError

admin.site.register(SiteConfiguration, SingletonModelAdmin)