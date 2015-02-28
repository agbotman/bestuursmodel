# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bestuursmodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='functietaak',
            options={'ordering': ['naam'], 'verbose_name': 'Taak', 'verbose_name_plural': 'Functietaken'},
        ),
        migrations.AlterModelOptions(
            name='taak',
            options={'ordering': ['nummer'], 'verbose_name_plural': 'Afdelingstaken'},
        ),
        migrations.AddField(
            model_name='functietaak',
            name='functietype',
            field=models.ForeignKey(blank=True, to='bestuursmodel.FunctieType', null=True),
            preserve_default=True,
        ),
    ]
