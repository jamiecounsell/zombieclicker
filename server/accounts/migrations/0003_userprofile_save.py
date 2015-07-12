# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150712_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='save',
            field=models.OneToOneField(null=True, blank=True, to='accounts.SaveState'),
        ),
    ]
