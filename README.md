# 🚲 Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Singkat
Proyek ini merupakan analisis data end-to-end yang bertujuan untuk mengeksplorasi tren penggunaan sepeda berdasarkan faktor cuaca, musim, dan waktu. Proyek ini mencakup proses data wrangling, exploratory data analysis (EDA), visualisasi data, hingga penerapan Machine Learning sederhana untuk memberikan insight yang mendukung pengambilan keputusan operasional.

## Dataset
Dataset yang digunakan dalam proyek ini adalah **Bike Sharing Dataset**. Dataset ini berisi riwayat penyewaan sepeda harian selama tahun 2011 dan 2012 beserta kondisi lingkungan sekitarnya.

## Struktur Folder
- `/dashboard`: Berisi file `dashboard.py` dan data yang telah dibersihkan untuk dashboard Streamlit.
- `/data`: Berisi file dataset mentah (`day.csv` dan `hour.csv`).
- `notebook.ipynb`: File analisis data utama yang mencakup proses wrangling hingga ML.
- `requirements.txt`: Daftar library Python yang diperlukan.
- `README.md`: Dokumentasi proyek ini.

## Cara Menjalankan
### 1. Menjalankan Notebook Analisis
Untuk melihat proses analisis lengkap, buka file `notebook.ipynb` di lingkungan Jupyter Notebook atau Google Colab.

### 2. Menjalankan Dashboard Streamlit
Pastikan Anda memiliki Python yang terinstal, kemudian jalankan langkah berikut di terminal atau command prompt:

1.  **Instalasi Library**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Menjalankan Dashboard**:
    ```bash
    streamlit run dashboard.py
    ```
    Atau jika file berada di folder tertentu:
    ```bash
    streamlit run dashboard/dashboard.py
    ```

## Ringkasan Insight Hasil Analisis
Berdasarkan hasil analisis data, berikut adalah temuan utama:
- **Pola Musiman**: Penyewaan sepeda mencapai volume tertinggi pada musim **Gugur (Fall)**, diikuti oleh musim Panas.
- **Pengaruh Cuaca**: Terdapat korelasi positif yang kuat antara suhu dan jumlah penyewa. Semakin hangat cuaca, semakin tinggi minat masyarakat untuk bersepeda.
- **Prediksi Machine Learning**: Dengan menggunakan Linear Regression, variabel suhu terbukti menjadi faktor prediktor paling signifikan dalam menentukan jumlah penyewaan harian.

## Screenshot Dashboard
![Dashboard Preview](https://drive.google.com/file/d/1gQfWOr7xuMcRUZ5GttMMKVmEsV35aX9l/view?usp=sharing)

---
*Proyek ini dibuat sebagai bagian dari seleksi GDGOC Universitas Sriwijaya.*
