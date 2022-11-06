from django.db import models

class Peserta(models.Model):
    nama = models.CharField(max_length=255)
    angkatan = models.IntegerField()
    jurusan = models.TextField()
    divisi_sbf = models.TextField()