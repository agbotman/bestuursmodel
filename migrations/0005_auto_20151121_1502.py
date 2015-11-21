# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def move_functies_to_m2m(apps, schema_editor):
    Functie = apps.get_model("bestuursmodel", "Functie")
    Afdeling_Functie = apps.get_model("bestuursmodel", "Afdeling_Functie")
    for functie in Functie.objects.all():
        Afdeling_Functie.objects.create(afdeling=functie.afdeling, functie=functie)

class Migration(migrations.Migration):

    dependencies = [
        ('bestuursmodel', '0004_auto_20151121_1425'),
    ]

    operations = [
        migrations.RunPython(move_functies_to_m2m),
    ]
