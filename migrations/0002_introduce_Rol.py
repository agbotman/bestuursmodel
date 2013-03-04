# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rol'
        db.create_table('bestuursmodel_rol', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('afdeling', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestuursmodel.Afdeling'])),
            ('functie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestuursmodel.Functie'])),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bestuursmodel', ['Rol'])


    def backwards(self, orm):
        # Deleting model 'Rol'
        db.delete_table('bestuursmodel_rol')


    models = {
        'bestuursmodel.afdeling': {
            'Meta': {'ordering': "['nummer']", 'object_name': 'Afdeling'},
            'einddatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'functies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bestuursmodel.Functie']", 'through': "orm['bestuursmodel.AfdelingFunctie']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'nummer': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'permanent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rapporteert_aan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'commissies'", 'null': 'True', 'to': "orm['bestuursmodel.Afdeling']"}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'functies'", 'null': 'True', 'to': "orm['bestuursmodel.Sector']"}),
            'startdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'taakbeschrijving': ('django.db.models.fields.TextField', [], {})
        },
        'bestuursmodel.afdelingfunctie': {
            'Meta': {'object_name': 'AfdelingFunctie'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'functie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bestuursmodel.Functie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bestuursmodel.functie': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Functie'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'taken': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'functies'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['bestuursmodel.Taak']"}),
            'verantwoordelijkheden': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'functies'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['bestuursmodel.Verantwoordelijkheid']"})
        },
        'bestuursmodel.functieeis': {
            'Meta': {'ordering': "['naam']", 'object_name': 'FunctieEis'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'functies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'functie_eisen'", 'symmetrical': 'False', 'to': "orm['bestuursmodel.Functie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        'bestuursmodel.rol': {
            'Meta': {'object_name': 'Rol'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'functie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bestuursmodel.Functie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bestuursmodel.sector': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Sector'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kleur': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        'bestuursmodel.taak': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Taak'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        'bestuursmodel.verantwoordelijkheid': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Verantwoordelijkheid'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        }
    }

    complete_apps = ['bestuursmodel']
