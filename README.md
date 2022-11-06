## [PTI-BACKEND] MINI-PROJECT
Slide & Instruction Details:
<a href="https://github.com/eugeniusms/sbf-pti-be/blob/master/slides/Django%20SBF%20PTI%202022%20-%20By%20Eugenius%20Mario.pdf" target="_blank">
Download
</a>
<br>
by https://github.com/eugeniusms

## Cara Menjalankan Solusi:
1.  Salin repository ini ke komputer secara lokal<br>
    `git clone https://github.com/eugeniusms/sbf-pti-be`<br>
    Lalu masuk ke dalam folder proyek dengan<br>
    `cd sbf-pti-be`
2.  Buat venv baru bernama env<br>
    `python -m venv env`
3.  Menginstall dependensi proyek<br>
    `pip install -r requirements.txt`
4.  Menjalankan migrate<br>
    `python manage.py migrate`
5.  Menjalankan server<br>
    `python manage.py runserver`<br>
    Buka browser ke alamat<br>
    `localhost:8000/daftar-destinasi`
6.  Jika ingin menambahkan daftar peserta maka buat superuser<br>
    `python manage.py createsuperuser`<br>
    Lalu login melalui halaman admin dan tambahkan data di dalamnya<br>
    `localhost:8000/admin`

## Selamat Belajar 😁
Credit: <a href="https://github.com/eugeniusms">Eugenius Mario</a> - PTI 2022
