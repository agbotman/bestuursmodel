# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        from bestuursmodel.models import Afdeling
        Afdeling.objects.rebuild()
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'bestuursmodel.afdeling': {
            'Meta': {'object_name': 'Afdeling'},
            'einddatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'functies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bestuursmodel.Functie']", 'through': u"orm['bestuursmodel.Rol']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'nummer': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'permanent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rapporteert_aan': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'commissies'", 'null': 'True', 'to': u"orm['bestuursmodel.Afdeling']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'functies'", 'null': 'True', 'to': u"orm['bestuursmodel.Sector']"}),
            'startdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'taakbeschrijving': ('django.db.models.fields.TextField', [], {}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'bestuursmodel.functie': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Functie'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.functieeis': {
            'Meta': {'ordering': "['naam']", 'object_name': 'FunctieEis'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'functies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'functie_eisen'", 'symmetrical': 'False', 'to': u"orm['bestuursmodel.Functie']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.rol': {
            'Meta': {'object_name': 'Rol'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rollen'", 'to': u"orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {'default': "' '", 'null': 'True', 'blank': 'True'}),
            'functie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rollen'", 'to': u"orm['bestuursmodel.Functie']"}),
            'generieke_rol': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bestuursmodel.RolGeneriek']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bestuursmodel.rolgeneriek': {
            'Meta': {'object_name': 'RolGeneriek'},
            'beschrijving': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.sector': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Sector'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kleur': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.taak': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Taak'},
            'beschrijving': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'rollen': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'taken'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['bestuursmodel.Rol']"})
        },
        u'bestuursmodel.verantwoordelijkheid': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Verantwoordelijkheid'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'verantwoordelijkheden'", 'null': 'True', 'to': u"orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'verantwoordelijkheden'", 'null': 'True', 'to': u"orm['bestuursmodel.Rol']"})
        }
    }

    complete_apps = ['bestuursmodel']
    symmetrical = True
