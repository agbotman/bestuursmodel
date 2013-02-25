# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Afdeling'
        db.create_table('bestuursmodel_afdeling', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nummer', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('taakbeschrijving', self.gf('django.db.models.fields.TextField')()),
            ('rapporteert_aan', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='commissies', null=True, to=orm['bestuursmodel.Afdeling'])),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='functies', null=True, to=orm['bestuursmodel.Sector'])),
            ('permanent', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('startdatum', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('einddatum', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('bestuursmodel', ['Afdeling'])

        # Adding model 'Functie'
        db.create_table('bestuursmodel_functie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bestuursmodel', ['Functie'])

        # Adding M2M table for field taken on 'Functie'
        db.create_table('bestuursmodel_functie_taken', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('functie', models.ForeignKey(orm['bestuursmodel.functie'], null=False)),
            ('taak', models.ForeignKey(orm['bestuursmodel.taak'], null=False))
        ))
        db.create_unique('bestuursmodel_functie_taken', ['functie_id', 'taak_id'])

        # Adding M2M table for field verantwoordelijkheden on 'Functie'
        db.create_table('bestuursmodel_functie_verantwoordelijkheden', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('functie', models.ForeignKey(orm['bestuursmodel.functie'], null=False)),
            ('verantwoordelijkheid', models.ForeignKey(orm['bestuursmodel.verantwoordelijkheid'], null=False))
        ))
        db.create_unique('bestuursmodel_functie_verantwoordelijkheden', ['functie_id', 'verantwoordelijkheid_id'])

        # Adding model 'AfdelingFunctie'
        db.create_table('bestuursmodel_afdelingfunctie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('afdeling', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestuursmodel.Afdeling'])),
            ('functie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestuursmodel.Functie'])),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bestuursmodel', ['AfdelingFunctie'])

        # Adding model 'Taak'
        db.create_table('bestuursmodel_taak', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bestuursmodel', ['Taak'])

        # Adding model 'Verantwoordelijkheid'
        db.create_table('bestuursmodel_verantwoordelijkheid', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bestuursmodel', ['Verantwoordelijkheid'])

        # Adding model 'FunctieEis'
        db.create_table('bestuursmodel_functieeis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bestuursmodel', ['FunctieEis'])

        # Adding M2M table for field functies on 'FunctieEis'
        db.create_table('bestuursmodel_functieeis_functies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('functieeis', models.ForeignKey(orm['bestuursmodel.functieeis'], null=False)),
            ('functie', models.ForeignKey(orm['bestuursmodel.functie'], null=False))
        ))
        db.create_unique('bestuursmodel_functieeis_functies', ['functieeis_id', 'functie_id'])

        # Adding model 'Sector'
        db.create_table('bestuursmodel_sector', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('kleur', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bestuursmodel', ['Sector'])


    def backwards(self, orm):
        # Deleting model 'Afdeling'
        db.delete_table('bestuursmodel_afdeling')

        # Deleting model 'Functie'
        db.delete_table('bestuursmodel_functie')

        # Removing M2M table for field taken on 'Functie'
        db.delete_table('bestuursmodel_functie_taken')

        # Removing M2M table for field verantwoordelijkheden on 'Functie'
        db.delete_table('bestuursmodel_functie_verantwoordelijkheden')

        # Deleting model 'AfdelingFunctie'
        db.delete_table('bestuursmodel_afdelingfunctie')

        # Deleting model 'Taak'
        db.delete_table('bestuursmodel_taak')

        # Deleting model 'Verantwoordelijkheid'
        db.delete_table('bestuursmodel_verantwoordelijkheid')

        # Deleting model 'FunctieEis'
        db.delete_table('bestuursmodel_functieeis')

        # Removing M2M table for field functies on 'FunctieEis'
        db.delete_table('bestuursmodel_functieeis_functies')

        # Deleting model 'Sector'
        db.delete_table('bestuursmodel_sector')


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