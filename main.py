import streamlit as st
import os
import subprocess

# Judul utama aplikasi
st.title("Machine Learning Models")

# Menu utama: SVM dan Random Forest
menu = st.sidebar.selectbox("Select Model", ["SVM", "Random Forest"])

# Sub-menu berdasarkan pilihan model
if menu == "SVM":
    sub_menu = st.sidebar.selectbox("Select Dataset", ["Fish", "Fruit"])
    if sub_menu == "Fish":
        st.write("Running SVM for Fish...")
        # Jalankan aplikasi SVM/Fish/app.py
        subprocess.run(["streamlit", "run", "SVM/Fish/app.py"])
    elif sub_menu == "Fruit":
        st.write("Running SVM for Fruit...")
        # Jalankan aplikasi SVM/Fruit/app.py
        subprocess.run(["streamlit", "run", "SVM/Fruit/app.py"])
elif menu == "Random Forest":
    sub_menu = st.sidebar.selectbox("Select Dataset", ["Fish", "Fruit"])
    if sub_menu == "Fish":
        st.write("Running Random Forest for Fish...")
        # Jalankan aplikasi Random Forest/Fish/app.py
        subprocess.run(["streamlit", "run", "Random Forest/Fish/app.py"])
    elif sub_menu == "Fruit":
        st.write("Running Random Forest for Fruit...")
        # Jalankan aplikasi Random Forest/Fruit/app.py
        subprocess.run(["streamlit", "run", "Random Forest/Fruit/app.py"])
