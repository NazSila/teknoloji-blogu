from django.shortcuts import render, get_object_or_404, redirect

from .forms import YaziForm, IletisimForm, YorumForm
from .models import Yazi, IletisimMesaji
from django.db.models import Q
from django.contrib import messages

def ana_sayfa(request):
    yazilar = Yazi.objects.filter(yayinda_mi=True).order_by("-olusturulma_tarihi")
    return render(request, "posts/ana_sayfa.html", {"yazilar": yazilar})


def yazi_detay(request, id):
    yazi = get_object_or_404(Yazi, id=id)
    yorumlar = yazi.yorumlar.all().order_by("-olusturulma_tarihi")

    if request.method == "POST":
        form = YorumForm(request.POST)

        if form.is_valid():
            yorum = form.save(commit=False)
            yorum.yazi = yazi
            yorum.save()
            messages.success(request, "Yorumunuz başarıyla eklendi.")
            return redirect("yazi_detay", id=yazi.id)
    else:
        form = YorumForm()

    return render(request, "posts/yazi_detay.html", {
        "yazi": yazi,
        "yorumlar": yorumlar,
        "form": form,
    })


def yazi_ekle(request):
    if request.method == "POST":
        form = YaziForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Yazı başarıyla oluşturuldu.")
            return redirect("ana_sayfa")
    else:
        form = YaziForm()

    return render(request, "posts/yazi_form.html", {"form": form, "baslik": "Yazı Ekle"})


def yazi_guncelle(request, id):
    yazi = get_object_or_404(Yazi, id=id)

    if request.method == "POST":
        form = YaziForm(request.POST, instance=yazi)
        if form.is_valid():
            form.save()
            messages.success(request, "Yazı başarıyla güncellendi.")
            return redirect("yazi_detay", id=yazi.id)
    else:
        form = YaziForm(instance=yazi)

    return render(request, "posts/yazi_form.html", {"form": form, "baslik": "Yazı Güncelle"})


def yazi_sil(request, id):
    yazi = get_object_or_404(Yazi, id=id)

    if request.method == "POST":
        yazi.delete()
        messages.success(request, "Yazı başarıyla silindi.")
        return redirect("ana_sayfa")

    return render(request, "posts/yazi_sil.html", {"yazi": yazi})


def hakkimizda(request):
    return render(request, "posts/hakkimizda.html")


def iletisim(request):
    return render(request, "posts/iletisim.html")


def iletisim(request):
    if request.method == "POST":
        form = IletisimForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Mesajınız başarıyla gönderildi.")
            return redirect("ana_sayfa")
    else:
        form = IletisimForm()

    return render(request, "posts/iletisim.html", {"form": form})


def ana_sayfa(request):
    arama = request.GET.get("q", "")

    yazilar = Yazi.objects.filter(yayinda_mi=True)

    if arama:
        yazilar = yazilar.filter(
            Q(baslik__icontains=arama) |
            Q(ozet__icontains=arama) |
            Q(icerik__icontains=arama)
        )

    yazilar = yazilar.order_by("-olusturulma_tarihi")

    return render(request, "posts/ana_sayfa.html", {
        "yazilar": yazilar,
        "arama": arama,
    })

def ana_sayfa(request):
    arama = request.GET.get("q", "")

    yazilar = Yazi.objects.filter(yayinda_mi=True)

    if arama:
        yazilar = yazilar.filter(
            Q(baslik__icontains=arama) |
            Q(ozet__icontains=arama) |
            Q(icerik__icontains=arama)
        )

    yazilar = yazilar.order_by("-olusturulma_tarihi")

    toplam_yazi = Yazi.objects.count()
    toplam_mesaj = IletisimMesaji.objects.count()

    return render(request, "posts/ana_sayfa.html", {
        "yazilar": yazilar,
        "arama": arama,
        "toplam_yazi": toplam_yazi,
        "toplam_mesaj": toplam_mesaj,
    })