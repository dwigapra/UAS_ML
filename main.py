import streamlit as st
import runpy

def main():

    # Main menu options
    menu = ["SVM", "Random Forest", "Perceptron"]
    choice = st.sidebar.selectbox("Select Main Menu", menu)

    if choice == "SVM":
        svm_sub_menu()
    elif choice == "Random Forest":
        rf_sub_menu()
    elif choice == "Perceptron":
        p_sub_menu()

def svm_sub_menu():
    st.subheader("SVM Menu")

    # SVM submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
        st.write("Kamu memilih SVM -> Fish.")
        runpy.run_path('SVM/Fish/app.py')
    elif choice == "Fruit":
        st.write("Kamu memilih SVM -> Fruit.")
        runpy.run_path('SVM/Fruit/app.py')

def rf_sub_menu():
    st.subheader("Random Forest Menu")

    # Random Forest submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
        st.write("Kamu memilih Random Forest -> Fish.")
        runpy.run_path('Random Forest/Fish/app.py')
    elif choice == "Fruit":
        st.write("Kamu memilih Random Forest -> Fruit.")
        runpy.run_path('Random Forest/Fruit/app.py')

def p_sub_menu():
    st.subheader("Perceptron Menu")

    # Random Forest submenu options
    sub_menu = ["Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fruit":
        st.write("Perceptron -> Fruit.")
        runpy.run_path('Perceptron/Fruit/app.py')

if __name__ == "__main__":
    main()
