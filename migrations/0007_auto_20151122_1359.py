# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestuursmodel', '0006_remove_functie_afdeling'),
    ]

    operations = [
        migrations.RenameField('Afdeling', 'afdeling_functies', 'functies'),
    ]
