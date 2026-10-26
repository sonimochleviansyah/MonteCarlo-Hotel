import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Simulasi Monte Carlo - Hotel Cancellation Risk",
    layout="wide"
)

st.title(" Simulasi Monte Carlo: Estimasi Kerugian Pembatalan Hotel")
st.write("Aplikasi ini mengestimasi risiko kerugian finansial akibat pembatalan pemesanan hotel menggunakan metode Simulasi Monte Carlo.")

# 1. Load Data & Extraction Parameter


@st.cache_data
def load_data():
    df = pd.read_csv('hotel_bookings.csv')
    df_clean = df[df['adr'] > 0].copy()
    return df_clean


df_clean = load_data()

mean_adr = df_clean['adr'].mean()
std_adr = df_clean['adr'].std()
cancellation_rate = df_clean['is_canceled'].mean()

# Sidebar Input
st.sidebar.header("⚙️ Parameter Simulasi")

# Gunakan NIM kamu sebagai Default Seed
nim_seed = st.sidebar.number_input(
    "NIM Seed (Random Seed)", value=301240030, step=1)
num_simulations = st.sidebar.slider(
    "Jumlah Iterasi Simulasi", min_value=1000, max_value=20000, value=5000, step=1000)
num_bookings = st.sidebar.number_input(
    "Jumlah Pesanan Baru (Skenario)", value=100, step=10)
threshold_loss = st.sidebar.number_input(
    "Threshold Kerugian ($)", value=5000.0, step=500.0)

# 2. Jalankan Simulasi Monte Carlo
np.random.seed(nim_seed)

simulated_losses = []
for _ in range(num_simulations):
    prices = np.random.normal(mean_adr, std_adr, num_bookings)
    prices = np.maximum(prices, 0)  # Mencegah harga negatif
    is_canceled = np.random.rand(num_bookings) < cancellation_rate
    total_loss = np.sum(prices[is_canceled])
    simulated_losses.append(total_loss)

simulated_losses = np.array(simulated_losses)

# 3. Hitung Analisis Risiko
exceeded_count = np.sum(simulated_losses > threshold_loss)
risk_probability = (exceeded_count / num_simulations) * 100

# 4. Tampilkan Metrics Ringkasan
col1, col2, col3, col4 = st.columns(4)
col1.metric("Rata-rata ADR (μ)", f"${mean_adr:.2f}")
col2.metric("Std Dev ADR (σ)", f"${std_adr:.2f}")
col3.metric("Cancellation Rate", f"{cancellation_rate*100:.2f}%")
col4.metric("Probabilitas Kerugian > $" +
            f"{threshold_loss:,.0f}", f"{risk_probability:.2f}%")

st.markdown("---")

# 5. Visualisasi Hasil Simulasi
st.subheader("📊 Distribusi Hasil Simulasi Monte Carlo")

fig, ax = plt.subplots(figsize=(10, 4.5))
sns.histplot(simulated_losses, kde=True, color='crimson', bins=40, ax=ax)
ax.axvline(threshold_loss, color='black', linestyle='--', linewidth=2,
           label=f'Threshold Risiko (${threshold_loss:,.0f})')
ax.set_title("Visualisasi Risiko Kerugian Pembatalan Hotel")
ax.set_xlabel("Total Kerugian ($)")
ax.set_ylabel("Frekuensi Skenario")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

st.pyplot(fig)

# Kesimpulan Ringkas
st.subheader("💡 Kesimpulan Risk Analyst")
st.write(f"""
Berdasarkan **{num_simulations:,}** iterasi simulasi Monte Carlo dengan seed NIM **{nim_seed}**:
* Dari **{num_bookings}** proyeksi pesanan kamar baru, potensi total kerugian akibat pembatalan pemesanan memiliki probabilitas sebesar **{risk_probability:.2f}%** untuk melampaui batas anggaran risiko sebesar **${threshold_loss:,.2f}**.
""")
