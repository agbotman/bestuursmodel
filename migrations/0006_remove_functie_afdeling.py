# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestuursmodel', '0005_auto_20151121_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='functie',
            name='afdeling',
        ),
    ]
