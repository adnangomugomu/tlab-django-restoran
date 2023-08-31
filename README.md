# Restoran API

Ini adalah proyek API untuk kebutuhan restoran, yang mencakup manajemen bahan, kategori, dan resep makanan.


## Installation

jalankan projek dengan perintah docker-compose, pastikan port 8000 dan 3306 tidak digunakan oleh aplikasi lainnya.

```bash
  cd tlab-django-restoran
  docker-compose up --build -d
```
Tunggu sampai proses pembuatan container selesai
kemudian silahkan import Collection Postman.

```bash
    http://localhost:8000/
```
docker-compose ini sudah saya lengkapi dengan pengecekan sampai proses pembuatan database selesai dan proses migrasi
secara normal aplikasi akan berjalan di link tersebut

## Deskripsi Proyek

Proyek ini dibangun menggunakan [Django](https://www.djangoproject.com/) dan [Django Rest Framework](https://www.django-rest-framework.org/). Ini menyediakan RESTful API untuk:

- Manajemen bahan-bahan yang digunakan dalam berbagai resep makanan.
- Manajemen kategori untuk mengelompokkan resep makanan.
- Manajemen resep makanan, termasuk informasi tentang bahan dan kategori yang digunakan.

## Fitur Utama

- Membuat, membaca, memperbarui, dan menghapus bahan.
- Membuat, membaca, memperbarui, dan menghapus kategori.
- Membuat, membaca, memperbarui, dan menghapus resep makanan.
- Pencarian resep berdasarkan nama, bahan, dan kategori.

