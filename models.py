from django.db import models

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

class Rol(models.Model):
    afdeling = models.ForeignKey("Afdeling",
                                 related_name="rol_in_afdeling")
    functie = models.ForeignKey("Functie",
                                related_name="rol_van_functie")
    beschrijving = models.TextField("Rolbeschrijving")

    class Meta:
        verbose_name_plural = "Rollen"

    def __unicode__(self):
        return "Rol van %s in %s" %(self.functie.naam, self.afdeling.naam)


class Taak(models.Model):
    naam = models.CharField(max_length=45, unique=True)
    beschrijving = models.TextField("Taakbeschrijving")
    rol = models.ForeignKey("Taak",
                            blank=True, null=True)

    class Meta:
        ordering = ["naam"]
        verbose_name_plural = "Taken"

    def __unicode__(self):
        return self.naam


class Verantwoordelijkheid(models.Model):
    naam = models.CharField(max_length=45, unique=True)
    beschrijving = models.TextField("beschrijving")

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

