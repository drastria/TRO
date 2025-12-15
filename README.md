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

