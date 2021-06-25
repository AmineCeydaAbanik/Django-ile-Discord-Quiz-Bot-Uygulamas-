from django.db import models

class KategoriModel(models.Model):
    class Meta:
        verbose_name="Kategori"
        verbose_name_plural="Kategoriler"

    isim = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return self.isim

class SoruModel(models.Model):
    class Meta:
        verbose_name="Soru"
        verbose_name_plural="Sorular"

    baslik   = models.CharField(verbose_name="Başlık", max_length=255, blank=False)
    kategori = models.ForeignKey(KategoriModel, verbose_name="Kategori", on_delete=models.CASCADE , blank=False)

    def __str__(self):
        return self.baslik

class CevapModel(models.Model):
    class Meta:
        verbose_name="Cevap"
        verbose_name_plural="Cevaplar"

    soru    = models.ForeignKey  (SoruModel, related_name='cevap', verbose_name='Soru', on_delete=models.CASCADE, blank=False)
    cevap   = models.CharField   (verbose_name='Cevap', max_length=255, blank=False)
    dogruMu = models.BooleanField(verbose_name="Doğru cevap mı?", default=False)

    def __str__(self):
        return self.cevap