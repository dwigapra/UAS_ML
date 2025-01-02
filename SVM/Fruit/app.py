import streamlit as st
import pickle
import pandas as pd

# Load Model
try:
    with open('svm_model_fruit.pkl', 'rb') as model_file:
        svm_model = pickle.load(model_file)
    
    with open('svm_scaler_fruit.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
        
    model_loaded = True
except FileNotFoundError:
    st.error("File model atau scaler tidak ditemukan. Harap periksa path file.")
    model_loaded = False

# Judul aplikasi
st.title("Aplikasi Klasifikasi Jenis buah Orange vs Grapefuit")
st.write("Masukkan data buah.")

# Input fitur
diameter = st.number_input("Diameter (cm)", min_value=0.0)
weight = st.number_input("Weight (g)", min_value=0.0)
red = st.slider("Red Value", 0, 255)
green = st.slider("Green Value", 0, 255)
blue = st.slider("Blue Value", 0, 255)

# Prediksi
if st.button("Prediksi"):
    if model_loaded:
        # Pastikan input_data memiliki kolom yang sama dengan data yang digunakan untuk fitting scaler
        input_data = pd.DataFrame([[diameter, weight, red, green, blue]], 
                                  columns=['diameter', 'weight', 'red', 'green', 'blue'])
        
        # Scale data baru sebelum prediksi
        input_data_scaled = scaler.transform(input_data)
        
        # Prediksi menggunakan model
        prediction = svm_model.predict(input_data_scaled)
        st.write(f"Nama Buah: {prediction[0]}")
    else:
        st.error("Model atau scaler tidak berhasil dimuat.")
