# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestuursmodel', '0003_auto_20151103_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afdeling_Functie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('beschrijving', models.CharField(max_length=100)),
                ('afdeling', models.ForeignKey(to='bestuursmodel.Afdeling')),
                ('functie', models.ForeignKey(to='bestuursmodel.Functie')),
            ],
        ),
        migrations.AddField(
            model_name='afdeling',
            name='afdeling_functies',
            field=models.ManyToManyField(related_name='functie_afdelingen', through='bestuursmodel.Afdeling_Functie', to='bestuursmodel.Functie'),
        ),
    ]
