import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("all_data.csv")

# ======================
# TITLE
# ======================
st.title("🚲 Bike Sharing Dashboard")

# ======================
# FILTER DATA TYPE
# ======================
data_type = st.sidebar.selectbox(
    "Pilih Tipe Data",
    ["hour", "day"]
)

df = df[df['data_type'] == data_type]

# ======================
# KPI
# ======================
st.subheader("📊 Ringkasan")

col1, col2 = st.columns(2)
col1.metric("Rata-rata", int(df['cnt'].mean()))
col2.metric("Max", int(df['cnt'].max()))

# ======================
# WORKINGDAY
# ======================
st.subheader("Working Day vs Weekend")

avg_working = df.groupby('workingday')['cnt'].mean()

fig1, ax1 = plt.subplots()
ax1.bar(['Weekend', 'Working Day'], avg_working.values)

st.pyplot(fig1)

# ======================
# WEATHER
# ======================
st.subheader("Pengaruh Cuaca")

weather = df.groupby('weathersit')['cnt'].mean()

fig2, ax2 = plt.subplots()
sns.barplot(x=weather.index, y=weather.values, ax=ax2)

st.pyplot(fig2)

# ======================
# HOUR (kalau ada)
# ======================
if data_type == "hour" and 'hr' in df.columns:
    st.subheader("Pola Jam")

    hour_avg = df.groupby('hr')['cnt'].mean()

    fig3, ax3 = plt.subplots()
    ax3.plot(hour_avg.index, hour_avg.values)

    st.pyplot(fig3)


# ======================
# DATA
# ======================
with st.expander("Lihat Data"):
    st.dataframe(df.head())

st.markdown("""
### Insight:
- Penyewaan lebih tinggi pada hari kerja dibanding weekend  
- Cuaca cerah menghasilkan penyewaan tertinggi  
- Cuaca buruk menurunkan jumlah penyewaan secara signifikan  
""")

