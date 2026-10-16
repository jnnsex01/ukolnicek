from django.conf import settings
from django.db import models
from django.utils import timezone


class Ukol(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=200)
    popis = models.TextField(blank=True)
    vytvoreno = models.DateTimeField(default=timezone.now)
    termin = models.DateField(blank=True, null=True)
    splneno = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'úkol'
        verbose_name_plural = 'úkoly'

    def splnit(self):
        self.splneno = timezone.now()
        self.save()

    def __str__(self):
        return self.nazev