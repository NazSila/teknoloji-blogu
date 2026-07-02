from django import forms

from .models import Yazi, IletisimMesaji, Yorum


class YaziForm(forms.ModelForm):
    class Meta:
        model = Yazi
        fields = ["baslik", "ozet", "icerik", "gorsel_url", "yayinda_mi"]
        widgets = {
            "baslik": forms.TextInput(attrs={"class": "form-control"}),
            "ozet": forms.TextInput(attrs={"class": "form-control"}),
            "icerik": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
            "gorsel_url": forms.URLInput(attrs={"class": "form-control"}),
            "yayinda_mi": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimMesaji
        fields = ["ad_soyad", "eposta", "mesaj"]
        widgets = {
            "ad_soyad": forms.TextInput(attrs={"class": "form-control"}),
            "eposta": forms.EmailInput(attrs={"class": "form-control"}),
            "mesaj": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }


class YorumForm(forms.ModelForm):
    class Meta:
        model = Yorum
        fields = ["ad_soyad", "yorum"]
        widgets = {
            "ad_soyad": forms.TextInput(attrs={"class": "form-control"}),
            "yorum": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
