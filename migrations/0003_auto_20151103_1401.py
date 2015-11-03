# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestuursmodel', '0002_auto_20150201_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='functietaak',
            name='functies',
        ),
        migrations.AddField(
            model_name='functie',
            name='taken',
            field=models.ManyToManyField(to='bestuursmodel.FunctieTaak', through='bestuursmodel.FunctieTaakDetails'),
        ),
        migrations.AlterField(
            model_name='functietaakdetails',
            name='functie',
            field=models.ForeignKey(related_name='functietaakdetails', to='bestuursmodel.Functie'),
        ),
    ]
