# MetaDocAI

![Document Checker Banner](https://via.placeholder.com/700x200.png?text=MetaDocAI)

##  Deskripsi

**MetaDocAI** adalah aplikasi web interaktif yang memungkinkan pengguna untuk mengunggah dokumen `.docx` atau `.pdf` dan memeriksa apakah format dokumen tersebut sesuai dengan kriteria yang ditentukan. Aplikasi ini memeriksa aspek-aspek seperti font, ukuran font, spasi antar baris, dan margin dokumen untuk memastikan standar format yang konsisten.

##  Fitur

- **Pemeriksaan Dokumen `.docx` dan `.pdf`:** Mengunggah dan memeriksa dua format dokumen populer.
- **Validasi Font dan Ukuran Font:** Memastikan penggunaan font *Times New Roman* dengan ukuran 12 pt.
- **Validasi Spasi Antar Baris:** Memeriksa apakah spasi antar baris sesuai dengan standar 1.5.
- **Validasi Margin dalam Centimeter:** Memastikan margin dokumen sesuai dengan standar yang ditetapkan (Left: 4 cm, Right: 3 cm, Top: 3 cm, Bottom: 3 cm).
- **Antarmuka Pengguna Modern:** Desain responsif dan menarik menggunakan Bootstrap.
- **Umpan Balik Visual:** Menampilkan hasil pemeriksaan dengan ikon status yang jelas.
- **Pembatasan Ukuran File:** Membatasi ukuran file unggahan hingga 50MB untuk keamanan dan kinerja optimal.
- **Integrasi Machine Learning:** Menggunakan model ML untuk klasifikasi dokumen sebagai "Correct" atau "Incorrect".

##  Instalasi

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi ini di lingkungan lokal Anda:

### Prasyarat

- **Python 3.7+** terinstal di komputer Anda.
- **Git** terinstal di komputer Anda.

### Langkah-langkah

1. **Clone Repository**

    ```bash
    git clone https://github.com/Fapzarz/MetaDocAI.git
    cd MetaDocAI
    ```

2. **Buat dan Aktifkan Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Windows: venv\Scripts\activate
    ```

3. **Instal Dependensi**

    ```bash
    pip install -r requirements.txt
    ```

4. **Jalankan Aplikasi**

    ```bash
    python main.py
    ```

    **Akses Aplikasi**

    Buka browser Anda dan navigasikan ke `http://127.0.0.1:81/`

##  Penggunaan

### Buka Aplikasi

Setelah menjalankan aplikasi, buka URL yang diberikan (misalnya, `http://127.0.0.1:81/`) di browser Anda.

### Unggah Dokumen

Klik tombol "Choose File" dan pilih dokumen `.docx` atau `.pdf` yang ingin Anda periksa.

### Periksa Dokumen

Klik tombol "Periksa Dokumen". Spinner loading akan muncul menunjukkan bahwa dokumen sedang diproses.

### Lihat Hasil

Setelah proses selesai, hasil pemeriksaan akan ditampilkan di bawah formulir dengan informasi yang jelas mengenai aspek-aspek yang sesuai atau yang perlu diperbaiki.

##  Kontribusi

Kontribusi sangat diterima! Jika Anda menemukan bug atau memiliki saran fitur, silakan buka issue atau ajukan pull request.

##  Lisensi

MIT License

Copyright (c) 2024 Fapzarz

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

##  Kredit

Aplikasi ini dibuat oleh Fapzarz.

##  Catatan Pengembang

Integrasi Machine Learning akan tersedia segera, karena model sedang di training
Jika Anda mengalami masalah atau memiliki pertanyaan terkait proyek ini, jangan ragu untuk menghubungi saya melalui [fapzarz@gmail.com](mailto:fapzarz@gmail.com).

##  Changelog

### v1.3 - 2024-09-25

- **Integrasi Fitur Machine Learning:** Penambahan kemampuan klasifikasi dokumen menggunakan model ML untuk menentukan apakah dokumen sesuai atau tidak sesuai dengan kriteria yang ditentukan.
- **Penambahan Confidence Score:** Menampilkan skor kepercayaan dari prediksi ML untuk memberikan informasi lebih detail kepada pengguna.
- **Branding Proyek:** Mengubah nama aplikasi menjadi **MetaDocAI** dan memperbarui identitas branding di seluruh kode dan UI.
- **Peningkatan Keamanan:** Menambahkan langkah-langkah keamanan dalam penamaan ulang variabel dan fungsi serta penambahan metadata dalam kode untuk identifikasi proyek.
- **Perbaikan Error Handling:** Memperbaiki penanganan error pada upload dokumen untuk memberikan feedback yang lebih jelas kepada pengguna.
- **Penyempurnaan Antarmuka Pengguna:** Meningkatkan tampilan dan responsivitas UI dengan penambahan ikon status dan aktualisasi desain.


