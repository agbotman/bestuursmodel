# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bestuursmodel', '0007_auto_20151122_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afdeling',
            name='functies',
            field=models.ManyToManyField(related_name='afdelingen', through='bestuursmodel.Afdeling_Functie', to='bestuursmodel.Functie'),
        ),
        migrations.AlterField(
            model_name='afdeling',
            name='rapporteert_aan',
            field=mptt.fields.TreeForeignKey(related_name='afdelingen', blank=True, to='bestuursmodel.Afdeling', null=True),
        ),
        migrations.AlterField(
            model_name='afdeling',
            name='sector',
            field=models.ForeignKey(related_name='afdelingen', blank=True, to='bestuursmodel.Sector', null=True),
        ),
    ]
