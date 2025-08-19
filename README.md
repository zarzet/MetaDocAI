# MetaDocAI

**MetaDocAI** adalah aplikasi web modern berbasis AI untuk validasi format dokumen akademik dan profesional. Aplikasi ini menyediakan analisis komprehensif terhadap dokumen `.docx` dan `.pdf` dengan antarmuka yang clean dan professional.

## ✨ Fitur Utama

### 🎯 Validasi Dokumen
- **Pemeriksaan Multi-Format:** Mendukung dokumen `.docx` dan `.pdf`
- **Validasi Font:** Memeriksa jenis dan ukuran font (Times New Roman 12pt)
- **Validasi Spasi:** Menganalisis spasi antar baris (standar 1.5)
- **Validasi Margin:** Memeriksa margin dokumen dalam centimeter
- **Integrasi AI:** Klasifikasi dokumen dengan confidence score

### 🎨 Antarmuka Modern
- **Design System:** Menggunakan shadcn/ui design principles
- **Dark/Light Mode:** Toggle tema dengan deteksi sistem otomatis
- **Responsive Design:** Optimal di semua perangkat
- **Clean UI:** Tanpa emoji, professional appearance
- **Drag & Drop:** Upload file dengan drag and drop

### ⚙️ Pengaturan Kustom
- **Custom Margin:** Atur margin sesuai kebutuhan (tersimpan otomatis)
- **Flexible Spacing:** Konfigurasi spasi baris custom
- **Font Size Control:** Atur ukuran font yang diharapkan
- **Validation Tolerance:** Kontrol tingkat toleransi validasi
- **Feature Toggles:** Aktifkan/nonaktifkan fitur validasi tertentu

### 🚀 Batch Processing
- **Multi-File Upload:** Proses beberapa dokumen sekaligus
- **File Management:** Kelola daftar file dengan status individual
- **Batch Controls:** Tambah, hapus, atau clear semua file
- **Progress Tracking:** Monitor status setiap file dalam batch

### 📊 Pelaporan Detail
- **Kategorisasi Masalah:** Masalah dikelompokkan berdasarkan jenis
- **Visual Hierarchy:** Font issues di bagian bawah (karena tidak selalu akurat)
- **Detailed Reports:** Informasi spesifik untuk setiap masalah
- **Smart Warnings:** Peringatan khusus untuk deteksi font yang tidak akurat

## 🛠️ Teknologi

- **Backend:** Flask 3.1.1 (Python)
- **Document Processing:** python-docx 1.2.0, PyPDF2 3.0.1
- **Machine Learning:** scikit-learn 1.7.1, pandas 2.3.1
- **Frontend:** Vanilla JavaScript, Custom CSS
- **Storage:** localStorage untuk pengaturan persistent

## 📦 Instalasi

### Prasyarat
- **Python 3.7+**
- **Git**

### Langkah Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/zarzet/MetaDocAI.git
   cd MetaDocAI
   ```

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

## 🎮 Cara Penggunaan

### Upload Dokumen
1. **Drag & Drop** file ke area upload atau **klik untuk browse**
2. **Multi-file selection** - pilih beberapa dokumen sekaligus
3. **File validation** - otomatis filter file yang valid

### Konfigurasi Settings
1. **Klik icon gear** di pojok kiri atas
2. **Atur margin custom** sesuai kebutuhan
3. **Toggle fitur validasi** yang diinginkan
4. **Simpan pengaturan** (tersimpan otomatis)

### Analisis Dokumen
1. **Klik "Analisis dengan AI"**
2. **Monitor progress** setiap file
3. **Review hasil** yang dikategorisasi

### Interpretasi Hasil
- **✅ Success:** Dokumen sesuai semua standar
- **❌ Issues:** Masalah dikategorisasi (Spacing → Margin → Font)
- **⚠️ Font Warning:** Deteksi font tidak selalu akurat

## 🔧 Fitur Pengaturan

### Margin Kustom
- **Kiri:** 0-10cm (default: 4cm)
- **Kanan:** 0-10cm (default: 3cm)
- **Atas:** 0-10cm (default: 3cm)
- **Bawah:** 0-10cm (default: 3cm)

### Validasi Options
- **✅ Margin Check:** Validasi margin (default: ON)
- **✅ Spacing Check:** Validasi spasi baris (default: ON)
- **✅ Font Size Check:** Validasi ukuran font (default: ON)
- **❌ Font Type Check:** Validasi jenis font (default: OFF)

### Toleransi
- **Margin Tolerance:** 0-1cm (default: 0.1cm)
- **Spacing Tolerance:** Fixed 0.1 untuk konsistensi

## 📱 Antarmuka

### Design Principles
- **shadcn/ui inspired** - Clean, minimal, professional
- **HSL color system** - Consistent theming
- **Semantic colors** - Meaningful color usage
- **Accessible design** - WCAG compliant
- **Mobile responsive** - Works on all devices

### Theme Support
- **Light Mode:** Clean white background
- **Dark Mode:** Professional dark theme
- **System Detection:** Auto-detects OS preference
- **Persistent Choice:** Remembers user preference

## 🔄 Changelog

### v2.0 - 2025-01-20 (Major Update)

#### 🎨 UI/UX Overhaul
- **Complete redesign** dengan shadcn/ui principles
- **Removed all emojis** untuk tampilan yang lebih professional
- **Dark/Light mode** dengan system preference detection
- **Responsive improvements** untuk semua perangkat

#### ⚙️ Advanced Settings
- **Custom margin configuration** dengan persistent storage
- **Feature toggles** untuk enable/disable validasi tertentu
- **Tolerance settings** untuk kontrol validasi
- **Smart defaults** dengan font type check disabled

#### 🚀 Batch Processing
- **Multi-file upload** dengan drag & drop
- **File management system** dengan status tracking
- **Batch controls** untuk manipulasi file
- **Individual file removal** dari batch

#### 📊 Enhanced Reporting
- **Categorized issues** berdasarkan jenis masalah
- **Visual hierarchy** dengan font issues di bawah
- **Detailed error messages** dengan konteks yang jelas
- **Smart warnings** untuk deteksi yang tidak akurat

#### 🔧 Technical Improvements
- **Updated dependencies** ke versi terbaru
- **PyPDF2 integration** menggantikan PyMuPDF
- **Production-ready code** tanpa development comments
- **Improved error handling** dan validation

### v1.3 - 2024-09-25
- **Integrasi Machine Learning** untuk klasifikasi dokumen
- **Confidence Score** dari prediksi AI
- **Branding Update** ke MetaDocAI
- **Security Enhancements**
- **UI Improvements**

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:
1. Fork repository ini
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 Lisensi

Distributed under the MIT License. See `LICENSE` for more information.

## 👨‍💻 Developer

**Farraz Firdaus NA**
- Email: [fapzarz@gmail.com](mailto:fapzarz@gmail.com)
- GitHub: [@zarzet](https://github.com/zarzet)

## 🙏 Acknowledgments

- [shadcn/ui](https://ui.shadcn.com/) untuk design inspiration
- [Flask](https://flask.palletsprojects.com/) untuk web framework
- [python-docx](https://python-docx.readthedocs.io/) untuk document processing
- [scikit-learn](https://scikit-learn.org/) untuk machine learning capabilities

---

⭐ **Star this repository** jika berguna untuk Anda!