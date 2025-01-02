import streamlit as st
import pickle
import pandas as pd
import os

# Load Model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'svm_model_fruit.pkl')
scaler_path = os.path.join(current_dir, 'svm_scaler_fruit.pkl')

try:
    with open(model_path, 'rb') as model_file:
        svm_model = pickle.load(model_file)
except Exception as e:
    st.error(f"Error loading the model: {e}")

try:
    with open(scaler_path, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
except Exception as e:
    st.error(f"Error loading the scaler: {e}")

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
if svm_model and scaler:
    if st.button("Prediksi"):
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
