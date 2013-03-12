from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Afdeling(models.Model):
    nummer = models.PositiveIntegerField(unique=True)
    naam = models.CharField(max_length=45, unique=True)
    taakbeschrijving = models.TextField("Taakbeschrijving")
    rapporteert_aan = models.ForeignKey("Afdeling",
                                        related_name="commissies",
                                        blank=True, null=True)
    functies = models.ManyToManyField("Functie",
                                      through="Rol")
    sector = models.ForeignKey("Sector",
                                 related_name="functies",
                               blank=True, null=True)
    permanent = models.BooleanField(default=True)
    startdatum = models.DateField(blank=True, null=True)
    einddatum = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["nummer"]
        verbose_name_plural = "Afdelingen"

    def __unicode__(self):
        return self.naam

class Functie(models.Model):
    naam = models.CharField(max_length=45, unique=True)
    beschrijving = models.TextField("Functiebeschrijving")
    afdelingen = models.ManyToManyField("Afdeling",
                                      through="Rol")
    verantwoordelijkheden = models.ManyToManyField("Verantwoordelijkheid",
                                                  related_name="functies",
                                                   blank=True, null=True)
    class Meta:
        ordering = ["naam"]

    def __unicode__(self):
        return self.naam

class RolGeneriek(models.Model):
    naam = models.CharField(max_length=45, unique=True)
    beschrijving = models.TextField("beschrijving",
                                    blank=True, null=True)

    class Meta:
        verbose_name_plural = "Generieke Rollen"
    
    def __unicode__(self):
        return self.naam


class Rol(models.Model):
    afdeling = models.ForeignKey("Afdeling",
                                 related_name="rollen")
    functie = models.ForeignKey("Functie",
                                related_name="rollen")
    generieke_rol = models.ForeignKey("RolGeneriek",
                                      blank=True, null=True)
    beschrijving = models.TextField("beschrijving", default= ' ',
                                    blank=True, null=True)

    class Meta:
        verbose_name_plural = "Rollen"

    def beschrijving1(self):
        out1 = ''
        if self.generieke_rol:
            out1 = self.generieke_rol.beschrijving  %(self.afdeling)   
        return ' '.join([out1, self.beschrijving])

    def __unicode__(self):
        return "Rol van %s in %s" %(self.functie.naam, self.afdeling.naam)


class Taak(models.Model):
    """
    Taken worden kunnen worden toegekend aan een rol of een afdeling
    """
    naam = models.CharField(max_length=45, unique=True)
    beschrijving = models.TextField("Taakbeschrijving")
    rol = models.ForeignKey(Rol,
                            related_name="taken",
                            blank=True, null=True)
    afdeling = models.ForeignKey(Afdeling,
                                 related_name='taken',
                                 blank=True, null=True)

    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Taken"

    def beschrijving1(self):
        try:
            out = self.beschrijving %(self.afdeling)
        except:
            out = self.beschrijving
        return out

    def __unicode__(self):
        return self.naam


class Verantwoordelijkheid(models.Model):
    """
    Verantwoordelijkheden worden kunnen worden toegekend aan een rol of een afdeling
    """
    naam = models.CharField(max_length=45, unique=True)
    beschrijving = models.TextField("beschrijving")
    rol = models.ForeignKey(Rol,
                            related_name="verantwoordelijkheden",
                            blank=True, null=True)
    afdeling = models.ForeignKey(Afdeling,
                                 related_name='verantwoordelijkheden',
                                 blank=True, null=True)

    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Verantwoordelijkheden"

    def __unicode__(self):
        return self.naam


class FunctieEis(models.Model):
    naam = models.CharField(max_length=45, unique=True)
    beschrijving = models.TextField("beschrijving")
    functies = models.ManyToManyField("Functie",
                                      related_name="functie_eisen")
    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Functie-eisen"

    def __unicode__(self):
        return self.naam


class Sector(models.Model):
    naam = models.CharField(max_length=45, unique=True)
    kleur = models.CharField(max_length=15)
    beschrijving = models.TextField("beschrijving")
    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Sectoren"

    def __unicode__(self):
        return self.naam

