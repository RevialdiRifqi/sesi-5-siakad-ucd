# Perancangan UI/UX Sistem Informasi Akademik Berbasis Web (User-Centered Design)

Studi kasus penerapan materi **Sesi 5: Interaksi Manusia dan Komputer (IMK)**.

> Persona, data nilai, dan hasil usability di repositori ini adalah **simulasi** untuk memperagakan alur UCD.
> Untuk penelitian sebenarnya, ganti dengan hasil wawancara dan pengujian dengan mahasiswa nyata.

## 1. Latar Belakang dan Masalah
Banyak SIAKAD menyajikan informasi dalam tabel padat dan menu bertingkat sehingga mahasiswa sulit menemukan IPK, nilai,
atau melihat perkembangan studinya. **Rumusan masalah:** bagaimana merancang antarmuka SIAKAD yang sederhana, konsisten,
dan mudah dipahami berdasarkan kebutuhan mahasiswa?

## 2. Keterkaitan dengan Materi Pemateri
| Materi Sesi 5 | Penerapan di prototipe (`index.html`) |
|---|---|
| Aspek kognitif, beban kognitif | Informasi dipecah menjadi kartu kecil (3 ringkasan utama) agar tidak membebani memori kerja |
| Prinsip Gestalt: *proximity* | Elemen terkait dikelompokkan dalam satu kartu dengan jarak antarkartu yang jelas |
| Gestalt: *similarity* | Semua kartu, tombol, dan badge memakai gaya yang sama untuk fungsi yang sama |
| Warna, ukuran, bentuk | Angka IPK berukuran besar sebagai fokus; status memakai **warna + ikon + teks**, bukan warna saja |
| Aksesibilitas | Tautan "lewati ke konten", fokus keyboard terlihat, target sentuh min. 44px, kontras warna, mode gelap, `aria-label` pada grafik |
| Privasi dan etika | Hanya menampilkan data milik pengguna sendiri; tidak ada data pihak lain; prototipe memakai data dummy |
| Konteks penggunaan | Responsif (ponsel dan desktop) karena mahasiswa sering mengakses dari ponsel |
| Proses desain: analisis kebutuhan, prototipe, evaluasi | Bagian 3 sampai 6 di bawah |
| Visualisasi: grafik garis untuk tren | Tren IPS per semester |
| Visualisasi: grafik batang untuk perbandingan | Nilai antar mata kuliah (dengan garis batas 2,0) |
| Visualisasi: scatter plot untuk hubungan | Kehadiran vs nilai |
| Dasbor: ringkasan, filter, detail sesuai kebutuhan | Kartu ringkasan, filter semester, tombol "Lihat" untuk detail mata kuliah |

## 3. Riset Pengguna
**Metode:** wawancara (5 mahasiswa), observasi (mengamati cara mereka mencari nilai di SIAKAD lama), kuesioner awal.

Contoh pertanyaan wawancara:
1. Informasi apa yang paling sering Anda cari di SIAKAD? Seberapa sering?
2. Ceritakan terakhir kali Anda kesulitan menemukan sesuatu. Apa yang terjadi?
3. Perangkat apa yang biasa dipakai, dan di mana?
4. Apa yang Anda harapkan agar lebih mudah?

### User Persona (simulasi)
**Budi Santoso, 20 tahun, mahasiswa semester 4 Teknik Informatika**
- **Tujuan:** memantau IPK dan memastikan SKS cukup untuk lulus tepat waktu.
- **Kebiasaan:** membuka SIAKAD lewat ponsel, biasanya saat jeda kuliah atau menjelang KRS.
- **Masalah:** menu terlalu banyak, harus membuka beberapa halaman untuk melihat nilai, tidak ada gambaran tren IPS.
- **Kutipan:** "Saya cuma mau tahu IPK saya aman atau tidak, kok harus klik lima kali."

## 4. Analisis Kebutuhan
| ID | Kebutuhan (user story) | Prioritas |
|---|---|---|
| K1 | Sebagai mahasiswa, saya ingin melihat IPK dan SKS langsung di halaman utama | Tinggi |
| K2 | Saya ingin melihat tren IPS agar tahu perkembangan studi saya | Tinggi |
| K3 | Saya ingin menyaring nilai per semester | Sedang |
| K4 | Saya ingin detail satu mata kuliah tanpa pindah halaman | Sedang |
| K5 | Saya ingin bisa memakai sistem dari ponsel dan dengan keyboard | Tinggi |

## 5. Desain dan Prototipe
Prototipe fidelitas tinggi berupa satu file HTML tanpa library eksternal (grafik digambar dengan SVG):
```bash
# cukup buka file ini di browser, atau:
python -m http.server 8000     # lalu buka http://localhost:8000
```
Di Codespaces, buka `index.html` dengan ekstensi Live Server atau jalankan perintah `http.server` di atas.

## 6. Evaluasi Usability
**Skenario tugas:** (1) lihat IPK, (2) cari nilai mata kuliah tertentu, (3) bandingkan IPS antar semester.
**Metrik:** task success rate, waktu penyelesaian, dan kuesioner **SUS** (System Usability Scale, 10 pertanyaan skala 1 sampai 5).

```bash
pip install pandas
python analisis_usability.py
```
Hasil simulasi (5 responden):

| Ukuran | Hasil |
|---|---|
| Rata-rata SUS | 82,5 (kategori Excellent; batas "baik" = 68) |
| Lihat IPK | berhasil 100%, rata-rata 7,8 detik |
| Cari nilai mata kuliah | berhasil 80%, rata-rata 27,6 detik |
| Bandingkan IPS | berhasil 100%, rata-rata 13,4 detik |

**Temuan dan iterasi:** satu responden gagal pada tugas 2 karena mengira filter semester hanya mempengaruhi grafik.
Perbaikan: teks bantu "Grafik dan tabel mengikuti pilihan ini" ditambahkan di samping filter. Putaran uji berikutnya perlu mengukur ulang.

## 7. Struktur Berkas
```
index.html               prototipe dasbor
analisis_usability.py    hitung SUS dan kinerja tugas
data/                    data simulasi hasil uji (CSV)
```

## 8. Keterbatasan dan Pengembangan
- Sampel kecil dan simulasi; perlu pengujian dengan pengguna nyata, termasuk pengguna disabilitas (screen reader).
- Pengembangan: integrasi dengan backend Laravel dan autentikasi, halaman KRS dan jadwal, serta wireframe di Figma sebagai dokumentasi.
