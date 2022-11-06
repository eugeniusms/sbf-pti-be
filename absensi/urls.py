from django.urls import path
from absensi.views import daftar_peserta

app_name = 'absensi'

urlpatterns = [
    path('', daftar_peserta , name='daftar_peserta'), # http://localhost:8000/todolist/
]