import streamlit as st
import pandas as pd
import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Konfigurasi Halaman Modern
st.set_page_config(page_title="Bike Sharing Insight Dashboard", page_icon="🚲", layout="wide")

# 2. Fungsi Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('day.csv')
    df['dteday'] = pd.to_datetime(df['dteday'])
    # Mapping agar tampilan di dashboard lebih rapi
    df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    df['year'] = df['dteday'].dt.year # Tambah kolom tahun untuk filter cepat
    return df

df = load_data()

# 3. SIDEBAR (LOGIKA FILTER YANG LEBIH RAPI)
st.sidebar.image("https://img.icons8.com/clouds/100/000000/bicycle.png")
st.sidebar.title("🚲 Filter Analysis")

# Filter 1: Pilih Tahun (Lebih cepat daripada klik kalender satu per satu)
selected_year = st.sidebar.multiselect(
    "Pilih Tahun:", 
    options=df['year'].unique(), 
    default=df['year'].unique()
)

# Filter 2: Pilih Rentang Tanggal dengan Dua Kolom
st.sidebar.markdown("---")
st.sidebar.subheader("Rentang Waktu Detail")
col_date1, col_date2 = st.sidebar.columns(2)

with col_date1:
    start_date = st.date_input("Mulai", value=df['dteday'].min(), min_value=df['dteday'].min(), max_value=df['dteday'].max())

with col_date2:
    end_date = st.date_input("Selesai", value=df['dteday'].max(), min_value=df['dteday'].min(), max_value=df['dteday'].max())

# --- PROSES FILTER DATA ---
main_df = df[
    (df["year"].isin(selected_year)) & 
    (df["dteday"] >= pd.to_datetime(start_date)) & 
    (df["dteday"] <= pd.to_datetime(end_date))
]

# 4. HEADER & KPI METRICS
st.title("🚲 Bike Sharing Analytics Dashboard")
st.markdown(f"Menganalisis data penyewaan dari tahun **{', '.join(map(str, selected_year))}**.")

col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
col_kpi1.metric("Total Penyewa", f"{main_df['cnt'].sum():,}")
col_kpi2.metric("Rata-rata Harian", f"{int(main_df['cnt'].mean()):,}")
col_kpi3.metric("Kondisi Cuaca Terbanyak", main_df['weathersit'].mode()[0] if not main_df.empty else "-")

st.divider()

# 5. VISUALISASI UTAMA
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Tren Penyewaan per Musim")
    # Menjawab Pertanyaan Bisnis 1 [cite: 33, 35]
    fig_season = px.bar(main_df.groupby('season')['cnt'].mean().reset_index(), 
                        x='season', y='cnt', color='season',
                        color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_season, use_container_width=True)

with col_right:
    st.subheader("🌡️ Korelasi Suhu & Penyewaan")
    # Menjawab Pertanyaan Bisnis 2 [cite: 33, 35]
    fig_temp = px.scatter(main_df, x='temp', y='cnt', trendline="ols", 
                          color_discrete_sequence=['#ff4b4b'])
    st.plotly_chart(fig_temp, use_container_width=True)

# 6. INSIGHT & KESIMPULAN [cite: 46, 47]
st.divider()
with st.expander("Klik untuk melihat Ringkasan Insight"):
    st.write(f"""
    - **Total Data Terpilih**: {len(main_df)} hari.
    - **Insight Musim**: Strategi operasional harus difokuskan pada musim **{main_df.groupby('season')['cnt'].mean().idxmax() if not main_df.empty else '-'}** karena permintaan tertinggi.
    - **Pengaruh Cuaca**: Terdapat tren positif antara suhu dan jumlah penyewaan; peningkatan suhu berkontribusi pada kenaikan volume bisnis.
    """)