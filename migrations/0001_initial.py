# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afdeling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nummer', models.PositiveIntegerField(unique=True)),
                ('naam', models.CharField(unique=True, max_length=45)),
                ('taakbeschrijving', models.TextField(verbose_name=b'Taakbeschrijving')),
                ('permanent', models.BooleanField(default=True)),
                ('startdatum', models.DateField(null=True, blank=True)),
                ('einddatum', models.DateField(null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rapporteert_aan', mptt.fields.TreeForeignKey(related_name='commissies', blank=True, to='bestuursmodel.Afdeling', null=True)),
            ],
            options={
                'ordering': ['naam'],
                'verbose_name_plural': 'Afdelingen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bevoegdheid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(unique=True, max_length=100)),
                ('beschrijving', models.TextField(verbose_name=b'beschrijving')),
                ('afdeling', models.ForeignKey(related_name='bevoegdheden', blank=True, to='bestuursmodel.Afdeling', null=True)),
            ],
            options={
                'ordering': ['naam'],
                'verbose_name_plural': 'Bevoegdheden',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Functie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(unique=True, max_length=100)),
                ('beschrijving', models.TextField(verbose_name=b'Functiebeschrijving')),
                ('afdeling', models.ForeignKey(related_name='functies', blank=True, to='bestuursmodel.Afdeling', null=True)),
            ],
            options={
                'ordering': ['naam'],
                'verbose_name_plural': 'Functies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FunctieEis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(unique=True, max_length=100)),
                ('beschrijving', models.TextField(verbose_name=b'beschrijving')),
                ('functies', models.ManyToManyField(related_name='functie_eisen', verbose_name=b'Functie eisen', to='bestuursmodel.Functie')),
            ],
            options={
                'ordering': ['naam'],
                'verbose_name_plural': 'Functie-eisen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FunctieTaak',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(unique=True, max_length=100)),
                ('beschrijving', models.TextField(null=True, verbose_name=b'Taakbeschrijving', blank=True)),
            ],
            options={
                'ordering': ['naam'],
                'verbose_name': 'Taak',
                'verbose_name_plural': 'Taken',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FunctieTaakDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uur_per_maand', models.IntegerField()),
                ('functie', models.ForeignKey(to='bestuursmodel.Functie')),
                ('functietaak', models.ForeignKey(verbose_name=b'taak', to='bestuursmodel.FunctieTaak')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FunctieType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ['naam'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(unique=True, max_length=100)),
                ('kleur', models.CharField(max_length=15)),
                ('beschrijving', models.TextField(verbose_name=b'beschrijving')),
            ],
            options={
                'ordering': ['naam'],
                'verbose_name_plural': 'Sectoren',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Taak',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(unique=True, max_length=100)),
                ('beschrijving', models.TextField(null=True, verbose_name=b'Taakbeschrijving', blank=True)),
                ('nummer', models.IntegerField(default=10)),
                ('afdeling', models.ForeignKey(related_name='taken', blank=True, to='bestuursmodel.Afdeling', null=True)),
            ],
            options={
                'ordering': ['nummer'],
                'verbose_name_plural': 'Taken',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verantwoordelijkheid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(unique=True, max_length=100)),
                ('beschrijving', models.TextField(verbose_name=b'beschrijving')),
                ('afdeling', models.ForeignKey(related_name='verantwoordelijkheden', blank=True, to='bestuursmodel.Afdeling', null=True)),
            ],
            options={
                'ordering': ['naam'],
                'verbose_name_plural': 'Verantwoordelijkheden',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='functietaak',
            name='functies',
            field=models.ManyToManyField(to='bestuursmodel.Functie', through='bestuursmodel.FunctieTaakDetails'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='functie',
            name='functietype',
            field=models.ForeignKey(blank=True, to='bestuursmodel.FunctieType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='afdeling',
            name='sector',
            field=models.ForeignKey(related_name='functies', blank=True, to='bestuursmodel.Sector', null=True),
            preserve_default=True,
        ),
    ]
