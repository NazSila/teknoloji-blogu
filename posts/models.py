from django.db import models


class Yazi(models.Model):
    baslik = models.CharField(max_length=200)
    ozet = models.CharField(max_length=300)
    icerik = models.TextField()
    gorsel_url = models.URLField(blank=True, null=True)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    yayinda_mi = models.BooleanField(default=True)

    def __str__(self):
        return self.baslik


class IletisimMesaji(models.Model):
    ad_soyad = models.CharField(max_length=100)
    eposta = models.EmailField()
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad_soyad

class Yorum(models.Model):
    yazi = models.ForeignKey(
        Yazi,
        on_delete=models.CASCADE,
        related_name="yorumlar"
    )

    ad_soyad = models.CharField(max_length=100)
    yorum = models.TextField()

    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad_soyad