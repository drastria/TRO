<div align="center">

# 🚚 Optimasi Biaya Transportasi Distribusi
### PT Sembako Jaya

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PuLP](https://img.shields.io/badge/PuLP-Linear_Programming-orange?style=for-the-badge)](https://coin-or.github.io/pulp/)
[![Excel](https://img.shields.io/badge/Microsoft_Excel-Solver-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/excel)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

*Teknik Riset Operasional - Universitas Pamulang*

[Tentang Proyek](#-tentang-proyek) •
[Fitur](#-fitur) •
[Instalasi](#-instalasi) •
[Penggunaan](#-penggunaan) •
[Hasil](#-hasil) •
[Tim](#-tim)

</div>

---

## 📌 Tentang Proyek

Proyek ini merupakan implementasi **Program Linear** untuk menyelesaikan masalah **Transportation Problem** pada PT Sembako Jaya, sebuah perusahaan distributor sembako yang beroperasi dengan 3 pabrik dan 4 gudang regional [file:2].

### 🎯 Tujuan

- Meminimalkan total biaya transportasi distribusi
- Memenuhi seluruh permintaan gudang regional
- Memanfaatkan kapasitas pabrik secara optimal
- Membandingkan solusi dari Python (PuLP) dan Excel Solver

### 📊 Problem Statement

| Entitas | Jumlah | Kapasitas/Permintaan |
|---------|--------|---------------------|
| Pabrik | 3 | 3.700 unit total |
| Gudang Regional | 4 | 3.700 unit total |
| Rute Distribusi | 12 | Biaya bervariasi (Rp 8.000 - Rp 13.000/unit) |

---

## ✨ Fitur

- ✅ **Model Program Linear** lengkap dengan variabel keputusan dan kendala
- ✅ **Dual Solver Implementation**: Python (PuLP) dan Excel Solver
- ✅ **Validasi Hasil** dengan perbandingan kedua metode
- ✅ **Dokumentasi Lengkap** dalam format laporan akademik
- ✅ **Analisis Sensitivitas** dan eksplorasi skenario alternatif
- ✅ **Open Source** dan mudah direplikasi

---

## 🚀 Instalasi

### Prerequisites

Pastikan sistem Anda sudah terinstall:

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Microsoft Excel dengan Solver add-in (opsional)

### Setup Python Environment



### Aktivasi Excel Solver

1. Buka Microsoft Excel
2. File → Options → Add-ins
3. Pilih "Solver Add-in" → Go
4. Centang "Solver Add-in" → OK

---

## 💻 Penggunaan

### Menjalankan Optimasi dengan Python


### Menggunakan Excel Solver

1. Buka file `excel.xlsx` [file:1]
2. Klik tab "Data" → "Solver"
3. Set Objective: Cell total biaya (minimize)
4. By Changing Variable Cells: Range alokasi distribusi
5. Subject to Constraints: Kendala pasokan dan permintaan
6. Solve

---

## 📈 Hasil

### Solusi Optimal

**Total Biaya Minimum:** **Rp 31.600.000,-** [file:2]

### Alokasi Distribusi Optimal

| Rute | Unit | Biaya/Unit | Total Biaya |
|------|------|------------|-------------|
| P1 → G3 | 1.200 | Rp 8.000 | Rp 9.600.000 |
| P2 → G1 | 900 | Rp 9.000 | Rp 8.100.000 |
| P2 → G4 | 100 | Rp 9.000 | Rp 900.000 |
| P3 → G2 | 800 | Rp 9.000 | Rp 7.200.000 |
| P3 → G3 | 100 | Rp 10.000 | Rp 1.000.000 |
| P3 → G4 | 600 | Rp 8.000 | Rp 4.800.000 |

### Validasi

✅ **Python (PuLP):** Rp 31.600.000,-  
✅ **Excel Solver:** Rp 31.600.000,-  
✅ **Hasil Identik:** Kedua metode menghasilkan solusi yang sama [file:2]

---

## 🔬 Metodologi

### Model Matematis

**Fungsi Tujuan:**

Minimize: Z = Σ Σ (biaya_ij × x_ij)

**Kendala:**

1. **Pasokan Pabrik:** Σ x_ij = supply_i untuk setiap pabrik i [file:2]
2. **Permintaan Gudang:** Σ x_ij = demand_j untuk setiap gudang j [file:2]
3. **Non-Negatif:** x_ij ≥ 0 untuk semua i, j [file:2]

---

## 📁 Struktur Repository



## 👥 Tim

**Kelas 05TPLM005 - Teknik Informatika**  
Universitas Pamulang | 2024/2025

| Nama | NIM |
|------|-----|
| Afrian Pamungkas | 231011402924 |
| Muhammad Haikal Ardhana | 231011402061 |
| Siti Nur Halimah | 231011402974 |

**Dosen Pengampu:**  
Agung Perdananto S.Kom., M. Kom.

---

## 📚 Referensi

- Taha, H. A. (2017). *Operations Research: An Introduction* (10th ed.). Pearson Education [web:4][web:7]
- Mitchell, S., et al. (2011). PuLP: A Linear Programming Toolkit for Python
- Winston, W. L., & Goldberg, J. B. (2004). *Operations Research: Applications and Algorithms*

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE) - lihat file LICENSE untuk detail.

---

## 🤝 Kontribusi

Kontribusi, issues, dan feature requests sangat diterima!  
Silakan buka [issues page](https://github.com/drastria/TRO/issues) jika Anda menemukan bug atau memiliki saran.

---

## ⭐ Acknowledgments

- Terima kasih kepada Universitas Pamulang atas fasilitas dan bimbingannya
- PuLP library untuk menyediakan tools Linear Programming yang powerful
- Komunitas open source yang terus berkontribusi pada pengembangan tools optimasi

---

<div align="center">

**Dibuat dengan ❤️ untuk mata kuliah Teknik Riset Operasional**

[![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=for-the-badge&logo=github)](https://github.com/drastroa/TRO)

</div>
