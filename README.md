# MetaDocAI

**MetaDocAI** adalah aplikasi web modern berbasis AI untuk validasi format dokumen akademik dan profesional. Aplikasi ini menyediakan analisis komprehensif terhadap dokumen `.docx` dan `.pdf` dengan antarmuka yang clean dan profesional.

---

## Fitur Utama

### Validasi Dokumen
- **Pemeriksaan Multi-Format:** Mendukung dokumen `.docx` dan `.pdf`
- **Validasi Font:** Memeriksa jenis dan ukuran font (Times New Roman 12pt)
- **Validasi Spasi:** Menganalisis spasi antar baris (standar 1.5)
- **Validasi Margin:** Memeriksa margin dokumen dalam centimeter
- **Integrasi AI:** Klasifikasi dokumen dengan confidence score

### Antarmuka Modern
- **Design System:** Menggunakan prinsip desain shadcn/ui
- **Dark/Light Mode:** Toggle tema dengan deteksi sistem otomatis
- **Responsive Design:** Optimal di semua perangkat
- **Clean UI:** Tanpa emoji, tampilan profesional
- **Drag & Drop:** Upload file dengan drag and drop

### Pengaturan Kustom
- **Custom Margin:** Atur margin sesuai kebutuhan (tersimpan otomatis)
- **Flexible Spacing:** Konfigurasi spasi baris kustom
- **Font Size Control:** Atur ukuran font yang diharapkan
- **Validation Tolerance:** Kontrol tingkat toleransi validasi
- **Feature Toggles:** Aktifkan atau nonaktifkan fitur validasi tertentu

### Batch Processing
- **Multi-File Upload:** Proses beberapa dokumen sekaligus
- **File Management:** Kelola daftar file dengan status individual
- **Batch Controls:** Tambah, hapus, atau clear semua file
- **Progress Tracking:** Monitor status setiap file dalam batch

### Pelaporan Detail
- **Kategorisasi Masalah:** Masalah dikelompokkan berdasarkan jenis
- **Visual Hierarchy:** Font issues di bagian bawah (karena tidak selalu akurat)
- **Detailed Reports:** Informasi spesifik untuk setiap masalah
- **Smart Warnings:** Peringatan khusus untuk deteksi font yang tidak akurat

---

## Teknologi

- **Backend:** Flask 3.1.1 (Python)
- **Document Processing:** python-docx 1.2.0, PyPDF2 3.0.1
- **Machine Learning:** scikit-learn 1.7.1, pandas 2.3.1
- **Frontend:** Vanilla JavaScript, Custom CSS
- **Storage:** localStorage untuk pengaturan persistent

---

## Instalasi

### Prasyarat
- **Python 3.7+**
- **Git**

### Langkah Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/zarzet/MetaDocAI.git
   cd MetaDocAI

2. **Setup Virtual Environment**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**

   ```bash
   python main.py
   ```

5. **Access Application**

   Buka browser: `http://127.0.0.1:81/`

---

## Cara Penggunaan

### Upload Dokumen

1. Drag & drop file ke area upload atau klik untuk browse.
2. Pilih beberapa dokumen sekaligus (multi-file selection).
3. File validation otomatis akan memfilter file yang valid.

### Konfigurasi Settings

1. Klik ikon pengaturan di pojok kiri atas.
2. Atur margin kustom sesuai kebutuhan.
3. Toggle fitur validasi yang diinginkan.
4. Pengaturan tersimpan otomatis di localStorage.

### Analisis Dokumen

1. Klik **"Analisis dengan AI"**.
2. Monitor progress setiap file.
3. Review hasil analisis yang dikategorisasi.

### Interpretasi Hasil

* **Success:** Dokumen sesuai semua standar.
* **Issues:** Masalah dikategorisasi (Spacing → Margin → Font).
* **Font Warning:** Deteksi font tidak selalu akurat.

---

## Fitur Pengaturan

### Margin Kustom

* **Kiri:** 0-10cm (default: 4cm)
* **Kanan:** 0-10cm (default: 3cm)
* **Atas:** 0-10cm (default: 3cm)
* **Bawah:** 0-10cm (default: 3cm)

### Validasi Options

* **Margin Check:** Validasi margin (default: ON)
* **Spacing Check:** Validasi spasi baris (default: ON)
* **Font Size Check:** Validasi ukuran font (default: ON)
* **Font Type Check:** Validasi jenis font (default: OFF)

### Toleransi

* **Margin Tolerance:** 0-1cm (default: 0.1cm)
* **Spacing Tolerance:** Fixed 0.1 untuk konsistensi

---

## Antarmuka

### Design Principles

* Terinspirasi dari **shadcn/ui**
* Menggunakan **HSL color system** untuk konsistensi tema
* **Semantic colors** untuk kejelasan visual
* **Accessible design** sesuai standar WCAG
* **Mobile responsive** untuk semua perangkat

### Theme Support

* **Light Mode:** Latar putih bersih
* **Dark Mode:** Tema gelap profesional
* **System Detection:** Deteksi otomatis preferensi OS
* **Persistent Choice:** Mengingat preferensi pengguna

---

## Changelog

### v2.0 - 2025-01-20 (Major Update)

#### UI/UX Overhaul

* Redesign total menggunakan prinsip desain shadcn/ui
* Menghapus seluruh emoji untuk tampilan profesional
* Mode gelap/terang dengan deteksi preferensi sistem
* Peningkatan responsivitas di semua perangkat

#### Advanced Settings

* Konfigurasi margin kustom dengan penyimpanan otomatis
* Feature toggles untuk kontrol validasi
* Toleransi validasi dapat disesuaikan
* Smart defaults dengan font type check nonaktif

#### Batch Processing

* Multi-file upload dengan drag & drop
* File management system dengan status tracking
* Batch controls untuk manipulasi file
* Dukungan penghapusan file individual

#### Enhanced Reporting

* Masalah dikategorisasi berdasarkan jenis
* Hierarki visual dengan font issues di bawah
* Pesan error lebih jelas dan kontekstual
* Smart warnings untuk deteksi yang tidak akurat

#### Technical Improvements

* Pembaruan dependencies ke versi terbaru
* Integrasi PyPDF2 menggantikan PyMuPDF
* Kode siap produksi tanpa komentar development
* Error handling dan validasi yang ditingkatkan

### v1.3 - 2024-09-25

* Integrasi Machine Learning untuk klasifikasi dokumen
* Confidence score untuk hasil prediksi AI
* Rebranding menjadi MetaDocAI
* Peningkatan keamanan dan tampilan antarmuka

---

## Kontribusi

Kontribusi sangat diterima.
Langkah-langkah untuk berkontribusi:

1. Fork repository ini.
2. Buat feature branch baru:

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit perubahan:

   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. Push ke branch:

   ```bash
   git push origin feature/AmazingFeature
   ```
5. Buat Pull Request.

---

## Lisensi

Didistribusikan di bawah lisensi **MIT License**.
Lihat file `LICENSE` untuk informasi lebih lanjut.

---

## Developer

**Farraz Firdaus NA**

* Email: [fapzarz@gmail.com](mailto:fapzarz@gmail.com)
* GitHub: [@zarzet](https://github.com/zarzet)

---

## Acknowledgments

* [shadcn/ui](https://ui.shadcn.com/) untuk inspirasi desain
* [Flask](https://flask.palletsprojects.com/) untuk framework web
* [python-docx](https://python-docx.readthedocs.io/) untuk pemrosesan dokumen
* [scikit-learn](https://scikit-learn.org/) untuk kemampuan machine learning

---

⭐ **Berikan bintang repository ini** jika proyek ini berguna bagi Anda!

```

---

Apakah kamu ingin saya buatkan **versi bilingual (Indonesia + English)** agar lebih profesional untuk audiens internasional di GitHub (misalnya MetaDocAI - Indonesian/English README toggle)?
```
