from django.shortcuts import render
from absensi.models import Peserta

def daftar_peserta(request):
    data = Peserta.objects.all()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)