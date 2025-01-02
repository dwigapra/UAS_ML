import streamlit as st
import subprocess

def run_script(script_path):
    # Menjalankan file Streamlit menggunakan subprocess
    subprocess.Popen(["streamlit", "run", script_path])

def main():
    st.title("Aplikasi Utama")

    # Menu utama
    menu = st.sidebar.selectbox("Menu Utama", ["SVM", "Random Forest"])

    if menu == "SVM":
        st.header("Menu SVM")
        sub_menu = st.radio("Pilih Dataset:", ["Fish", "Fruit"])

        if sub_menu == "Fish":
            if st.button("Buka Fish - SVM"):
                run_script("SVM/Fish/app.py")
        elif sub_menu == "Fruit":
            if st.button("Buka Fruit - SVM"):
                run_script("SVM/Fruit/app.py")

    elif menu == "Random Forest":
        st.header("Menu Random Forest")
        sub_menu = st.radio("Pilih Dataset:", ["Fish", "Fruit"])

        if sub_menu == "Fish":
            if st.button("Buka Fish - Random Forest"):
                run_script("Random Forest/Fish/app.py")
        elif sub_menu == "Fruit":
            if st.button("Buka Fruit - Random Forest"):
                run_script("Random Forest/Fruit/app.py")

if __name__ == "__main__":
    main()
