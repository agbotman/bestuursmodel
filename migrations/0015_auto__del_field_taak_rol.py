# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Taak.rol'
        db.delete_column('bestuursmodel_taak', 'rol_id')

        # Adding M2M table for field rollen on 'Taak'
        db.create_table('bestuursmodel_taak_rollen', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('taak', models.ForeignKey(orm['bestuursmodel.taak'], null=False)),
            ('rol', models.ForeignKey(orm['bestuursmodel.rol'], null=False))
        ))
        db.create_unique('bestuursmodel_taak_rollen', ['taak_id', 'rol_id'])


    def backwards(self, orm):
        # Adding field 'Taak.rol'
        db.add_column('bestuursmodel_taak', 'rol',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='taken', null=True, to=orm['bestuursmodel.Rol'], blank=True),
                      keep_default=False)

        # Removing M2M table for field rollen on 'Taak'
        db.delete_table('bestuursmodel_taak_rollen')


    models = {
        'bestuursmodel.afdeling': {
            'Meta': {'ordering': "['nummer']", 'object_name': 'Afdeling'},
            'einddatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'functies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bestuursmodel.Functie']", 'through': "orm['bestuursmodel.Rol']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'nummer': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'permanent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rapporteert_aan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'commissies'", 'null': 'True', 'to': "orm['bestuursmodel.Afdeling']"}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'functies'", 'null': 'True', 'to': "orm['bestuursmodel.Sector']"}),
            'startdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'taakbeschrijving': ('django.db.models.fields.TextField', [], {})
        },
        'bestuursmodel.functie': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Functie'},
            'afdelingen': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bestuursmodel.Afdeling']", 'through': "orm['bestuursmodel.Rol']", 'symmetrical': 'False'}),
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
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
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rollen'", 'to': "orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {'default': "' '", 'null': 'True', 'blank': 'True'}),
            'functie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rollen'", 'to': "orm['bestuursmodel.Functie']"}),
            'generieke_rol': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bestuursmodel.RolGeneriek']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bestuursmodel.rolgeneriek': {
            'Meta': {'object_name': 'RolGeneriek'},
            'beschrijving': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
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
            'beschrijving': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'rollen': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'taken'", 'symmetrical': 'False', 'to': "orm['bestuursmodel.Rol']"})
        },
        'bestuursmodel.verantwoordelijkheid': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Verantwoordelijkheid'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'verantwoordelijkheden'", 'null': 'True', 'to': "orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'verantwoordelijkheden'", 'null': 'True', 'to': "orm['bestuursmodel.Rol']"})
        }
    }

    complete_apps = ['bestuursmodel']