from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from landingpage.models import Barang,Tanaman,JenisTanaman

#Create your views here



def barang_view(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs': barangs,
    }

    return render(request,'tampil_brg.html',konteks)

def tanaman(request):
    tanaman=Tanaman.objects.all()

    konteks={
        'tanaman': tanaman,
    }

    return render(request,'uts/index.html',konteks)

def jenis_tanaman(request):
    jenis_tanaman=JenisTanaman.objects.all()

    konteks={
        'jenis_tanaman': jenis_tanaman,
    }

    return render(request,'uts/jenis_tanaman.html',konteks)