from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CevapModel, KategoriModel, SoruModel
from .serializers import rastgeleSoruSerializer
from django.utils.datastructures import MultiValueDictKeyError

class RastgeleSoru(APIView):

    def get(self, request, formate=None, **kwargs):
        try:
            if(len(request.GET['kategori'])>0):
                kategori = KategoriModel.objects.filter(isim__icontains=request.GET['kategori'])
                kategori = kategori[0]
                soru = SoruModel.objects.filter(kategori=kategori).order_by('?')[:1]
            else:
                soru = SoruModel.objects.filter().order_by('?')[:1]
        except MultiValueDictKeyError:
            soru = SoruModel.objects.filter().order_by('?')[:1]
        
        serializer = rastgeleSoruSerializer(soru, many=True)
        return Response(serializer.data)

def formlar(request):
    mesaj=""
    if(request.method=='POST'):
        if request.GET['ekle'] == 'soru':
            kategori = KategoriModel.objects.filter(isim=request.POST['txtKategori'])[0]
            soru = SoruModel(baslik=request.POST['txtSoru'],kategori=kategori)
            soru.save()

            cevap1 = CevapModel(soru=soru,cevap=request.POST['cevap1'])
            cevap2 = CevapModel(soru=soru,cevap=request.POST['cevap2'])
            cevap3 = CevapModel(soru=soru,cevap=request.POST['cevap3'])

            cevaplar = [cevap1,cevap2,cevap3]
            cevaplar[int(request.POST['dogruCevap'])].dogruMu=True

            for cevap in cevaplar:
                cevap.save()
            
            mesaj="<script>alert('Soru Eklendi!');</script>"

        elif request.GET['ekle'] == 'kategori':
            kategori = KategoriModel(isim=request.POST['isim'])
            kategori.save()
            mesaj="<script>alert('Kategori Eklendi!');</script>"

    #Kategorileri Çekme ve Arayüze gönderme
    kategorilerFromModel = KategoriModel.objects.all()
    kategoriler = []
    for kategori in kategorilerFromModel:
        kategoriler.append(kategori.isim)

    #Soruları Çekme ve Arayüze gönderme
    sorularModel = SoruModel.objects.all()
    sorular = []
    for soru in sorularModel:
        cevaplar = [[cevap.cevap,cevap.dogruMu] for cevap in CevapModel.objects.filter(soru=soru)]
        sorular.append([soru.baslik,soru.kategori,cevaplar])


    return render(request, "index.html", {'kategoriler': kategoriler, 'sorular':sorular, 'mesaj':mesaj})