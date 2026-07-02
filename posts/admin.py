from django.contrib import admin
from .models import Yazi, IletisimMesaji, Yorum

@admin.register(Yazi)
class YaziAdmin(admin.ModelAdmin):
    list_display = ("baslik", "olusturulma_tarihi", "yayinda_mi")
    list_filter = ("yayinda_mi", "olusturulma_tarihi")
    search_fields = ("baslik", "ozet", "icerik")


@admin.register(IletisimMesaji)
class IletisimMesajiAdmin(admin.ModelAdmin):
    list_display = ("ad_soyad", "eposta", "olusturulma_tarihi")
    search_fields = ("ad_soyad", "eposta", "mesaj")

@admin.register(Yorum)
class YorumAdmin(admin.ModelAdmin):
    list_display = ("ad_soyad", "yazi", "olusturulma_tarihi")
    search_fields = ("ad_soyad", "yorum")