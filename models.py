from django.db import models
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Afdeling(MPTTModel):
    nummer = models.PositiveIntegerField(unique=True)
    naam = models.CharField(max_length=45, unique=True)
    taakbeschrijving = models.TextField("Taakbeschrijving")
    rapporteert_aan = TreeForeignKey("Afdeling",
                                      related_name="afdelingen",
                                      blank=True, null=True)
    sector = models.ForeignKey("Sector",
                                 related_name="afdelingen",
                               blank=True, null=True)
    permanent = models.BooleanField(default=True)
    startdatum = models.DateField(blank=True, null=True)
    einddatum = models.DateField(blank=True, null=True)
    functies = models.ManyToManyField("Functie", through='Afdeling_Functie',
                                                related_name="afdelingen")

    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Afdelingen"

    class MPTTMeta:
        parent_attr = "rapporteert_aan"
        order_insertion_by = ["nummer"]

    def __unicode__(self):
        return self.naam

class Functie(models.Model):
    naam = models.CharField(max_length=100, unique=True)
    beschrijving = models.TextField("Functiebeschrijving")
    functietype = models.ForeignKey('FunctieType',
                                 blank=True, null=True)
    taken = models.ManyToManyField("FunctieTaak", through='FunctieTaakDetails')
                                 
    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Functies"
        
    def get_absolute_url(self):
        return reverse('functie-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.naam
        
class Afdeling_Functie(models.Model):
    """ To store the m2m relation between Afdeling and Functie
    """
    afdeling = models.ForeignKey(Afdeling)
    functie = models.ForeignKey(Functie)
    beschrijving = models.CharField(max_length=100)

class Taak(models.Model):
    """ Taak die behoort bij een afdeling
        Taken die behoren bij een functie worden opgeslagen in het model FunctieTaak
    """
    naam = models.CharField(max_length=100, unique=True)
    beschrijving = models.TextField("Taakbeschrijving",
                                    blank=True, null=True)
    nummer = models.IntegerField(default=10)
    afdeling = models.ForeignKey("Afdeling",
                                 related_name="taken",
                                 blank=True, null=True)

    class Meta:
        ordering = ["nummer"]
        verbose_name_plural = "Afdelingstaken"

    def __unicode__(self):
        return self.naam

class FunctieType(models.Model):
    naam = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["naam"]
    
    def __unicode__(self):
        return self.naam

        
class FunctieTaak(models.Model):
    """ Taak die behoort bij een Functie
        Taken die behoren bij een Afdeling worden opgeslagen in model Taak
    """
    naam = models.CharField(max_length=100, unique=True)
    beschrijving = models.TextField("Taakbeschrijving",
                                    blank=True, null=True)
    functietype = models.ForeignKey('FunctieType',
                                 blank=True, null=True)

    class Meta:
        ordering = ["naam"]
        verbose_name = "Taak"
        verbose_name_plural = "Functietaken"
    
    def __unicode__(self):
        return self.naam


class FunctieTaakDetails(models.Model):
    functietaak = models.ForeignKey("FunctieTaak", verbose_name="taak")
    functie = models.ForeignKey("Functie", related_name="functietaakdetails") 
    uur_per_maand = models.IntegerField()

class Verantwoordelijkheid(models.Model):
    """
    Verantwoordelijkheden worden kunnen worden toegekend aan een rol of een afdeling
    """
    naam = models.CharField(max_length=100, unique=True)
    beschrijving = models.TextField("beschrijving")
    afdeling = models.ForeignKey(Afdeling,
                                 related_name='verantwoordelijkheden',
                                 blank=True, null=True)

    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Verantwoordelijkheden"

    def __unicode__(self):
        return self.naam


class Bevoegdheid(models.Model):
    """
    Bevoegdheden worden kunnen worden toegekend aan een afdeling
    """
    naam = models.CharField(max_length=100, unique=True)
    beschrijving = models.TextField("beschrijving")
    afdeling = models.ForeignKey(Afdeling,
                                 related_name='bevoegdheden',
                                 blank=True, null=True)

    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Bevoegdheden"

    def __unicode__(self):
        return self.naam

class FunctieEis(models.Model):
    naam = models.CharField(max_length=100, unique=True)
    beschrijving = models.TextField("beschrijving")
    functies = models.ManyToManyField("Functie",
                                      related_name="functie_eisen",
                                      verbose_name="Functie eisen")
    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Functie-eisen"

    def __unicode__(self):
        return self.naam


class Sector(models.Model):
    naam = models.CharField(max_length=100, unique=True)
    kleur = models.CharField(max_length=15)
    beschrijving = models.TextField("beschrijving")
    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Sectoren"

    def __unicode__(self):
        return self.naam

