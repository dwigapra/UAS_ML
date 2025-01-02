import streamlit as st
import subprocess

# Fungsi untuk menjalankan aplikasi Streamlit
def run_streamlit_app(path):
    # Menjalankan aplikasi Streamlit sebagai proses baru
    subprocess.Popen(["python", "-m", "streamlit", "run", path])

# Judul utama
st.title("Dashboard Model Machine Learning")

# Menu utama
menu = st.sidebar.selectbox("Pilih Model", ["SVM", "Random Forest"])

# Submenu berdasarkan menu utama
if menu == "SVM":
    submenu = st.sidebar.radio("Pilih Submenu", ["Fish", "Fruit"])
    if submenu == "Fish":
        if st.button("Jalankan SVM Fish"):
            run_streamlit_app("SVM/Fish/app.py")
    elif submenu == "Fruit":
        if st.button("Jalankan SVM Fruit"):
            run_streamlit_app("SVM/Fruit/app.py")

elif menu == "Random Forest":
    submenu = st.sidebar.radio("Pilih Submenu", ["Fish", "Fruit"])
    if submenu == "Fish":
        if st.button("Jalankan Random Forest Fish"):
            run_streamlit_app("Random Forest/Fish/app.py")
    elif submenu == "Fruit":
        if st.button("Jalankan Random Forest Fruit"):
            run_streamlit_app("Random Forest/Fruit/app.py")
