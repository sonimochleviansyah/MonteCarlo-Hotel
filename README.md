# 🏨 Data-Driven Monte Carlo Simulation: Hotel Booking Cancellation Risk

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Aplikasi simulasi komputasi berbasis data menggunakan **Metode Monte Carlo** untuk mengestimasi risiko kerugian finansial akibat pembatalan pemesanan hotel (*Hotel Booking Cancellations Risk Assessment*). 

Projek ini disusun untuk memenuhi **Tugas Akhir 03 (TA-03)** pada mata kuliah **Pemodelan dan Simulasi (Semester 5)**.

---

## 📌 Identitas Mahasiswa
* **Nama:** Soni Moch Leviansyah
* **NIM:** 301240030
* **Program Studi:** Teknik Informatika
* **Fakultas:** Teknologi Informasi
* **Universitas:** Universitas Bale Bandung (UNIBBA)

---

## 🚀 Live Demo & Repository
* **Web App Streamlit Live:** [https://hotel-montecarlo.streamlit.app](https://hotel-montecarlo.streamlit.app)
* **GitHub Repository:** [https://github.com/sonimochleviansyah/MonteCarlo-Hotel](https://github.com/sonimochleviansyah/MonteCarlo-Hotel)

---

## 📊 Gambaran Studi Kasus & Dataset

Dataset yang digunakan berasal dari Kaggle: **[Hotel Booking Demand Dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)** oleh Jesse Mostipak.

### **Parameter Historis yang Diekstrak:**
1. **Average Daily Rate ($\mu$):** $\$103.53$ (Rata-rata tarif sewa kamar per malam)
2. **Standard Deviation ($\sigma$):** $\$49.20$ (Volatilitas/variasi harga kamar)
3. **Cancellation Rate:** $37.48\%$ (Rasio pembatalan pemesanan historis)

### **Metodologi Simulasi Monte Carlo:**
* **Jumlah Iterasi:** 5.000 skenario
* **Jumlah Pesanan (Proyeksi):** 100 pemesanan kamar baru
* **Random Seed:** `301240030` (Terkunci berdasarkan NIM Mahasiswa)
* **Distribusi Variabel:** Distribusi Normal $\mathcal{N}(\mu, \sigma^2)$ untuk harga kamar, dikombinasikan dengan Proses Bernoulli untuk status pembatalan.

---

## 💡 Hasil Analisis Risiko (Risk Assessment)

Berdasarkan simulasi sebanyak **5.000 iterasi**:
* **Rata-rata Estimasi Kerugian:** Berkisar pada rentang **$\$3.800 – \$4.000$**.
* **Threshold Risiko:** Diatur pada angka **$\$5.500$**.
* **Hasil Probabilitas:** Hanya **20 dari 5.000 skenario** yang melampaui batas *threshold* $\$5.500$.
* **Kesimpulan Risk Analyst:** Probabilitas terjadinya kerugian ekstrem melampaui batas anggaran adalah sebesar **$0,40\%$** (Sangat Aman / *Low Risk*).

---

## 📂 Struktur Repositori

```text
MonteCarlo-Hotel/
│
├── hotel_bookings.csv       # Dataset historis Kaggle
├── app.py                   # Source code utama aplikasi Streamlit (Web App)
├── ta03_simulation.ipynb    # Jupyter Notebook komputasi Monte Carlo & analisis
├── requirements.txt         # Daftar dependency library Python
└── README.md                # Dokumentasi projek
