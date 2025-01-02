import streamlit as st
import pickle
import pandas as pd
import os

# Load the Naive Bayes model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'svm_model_fish.pkl')
scaler_path = os.path.join(current_dir, 'svm_scaler_fish.pkl')

with open(model_path, 'rb') as model_file:
    svm_model = pickle.load(model_file)

with open(scaler_path, 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Judul aplikasi
st.title("Aplikasi Klasifikasi Jenis Ikan")
st.write("Masukkan data ikan untuk mengetahui spesiesnya.")

# Input fitur
length = st.number_input("Masukkan panjang ikan (cm):", min_value=0.0)
weight = st.number_input("Masukkan berat ikan (g):", min_value=0.0)
w_l_ratio = st.number_input("Masukkan rasio lebar-panjang ikan:", min_value=0.0, max_value=1.0)

# Prediksi
if st.button("Prediksi"):
    # Data input dari pengguna
    input_data = pd.DataFrame([[length, weight, w_l_ratio]], columns=['length', 'weight', 'w_l_ratio'])
        
    # Scale data baru sebelum prediksi
    input_data_scaled = scaler.transform(input_data)
    
    # Prediksi menggunakan model
    prediction = svm_model.predict(input_data_scaled)
    st.write(f"Spesies Ikan: {prediction[0]}")
else:
    st.error("Model atau scaler tidak berhasil dimuat.")
