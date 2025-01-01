import streamlit as st
import subprocess
import os

def main():
    st.title("Main Menu")

    # Main menu options
    menu = ["SVM", "Random Forest"]
    choice = st.sidebar.selectbox("Select Main Menu", menu)

    if choice == "SVM":
        svm_sub_menu()
    elif choice == "Random Forest":
        rf_sub_menu()

def svm_sub_menu():
    st.subheader("SVM Menu")

    # SVM submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
        st.write("You selected SVM -> Fish.")
        run_streamlit_app('RF/Fish/app.py')
    elif choice == "Fruit":
        st.write("You selected SVM -> Fruit.")
        run_streamlit_app('RF/Fish/app.py')

def rf_sub_menu():
    st.subheader("Random Forest Menu")

    # Random Forest submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
        st.write("You selected Random Forest -> Fish.")
        run_streamlit_app('RF/Fish/app.py')
    elif choice == "Fruit":
        st.write("You selected Random Forest -> Fruit.")
        run_streamlit_app('RF/Fish/app.py')

def run_streamlit_app(app_path):
    if os.path.exists(app_path):
        st.write(f"Running: {app_path}")
        subprocess.Popen(['streamlit', 'run', app_path], shell=True)
    else:
        st.error(f"File not found: {app_path}")

if __name__ == "__main__":
    main()
