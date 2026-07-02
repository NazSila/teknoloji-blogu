from django.urls import path
from . import views

urlpatterns = [
    path("", views.ana_sayfa, name="ana_sayfa"),
    path("yazi/<int:id>/", views.yazi_detay, name="yazi_detay"),
    path("yazi-ekle/", views.yazi_ekle, name="yazi_ekle"),
    path("yazi/<int:id>/guncelle/", views.yazi_guncelle, name="yazi_guncelle"),
    path("yazi/<int:id>/sil/", views.yazi_sil, name="yazi_sil"),
    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),
    path("iletisim/", views.iletisim, name="iletisim"),
]