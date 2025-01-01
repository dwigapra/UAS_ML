import streamlit as st
import os

def main():
    # Main menu options
    menu = ["SVM", "Random Forest"]
    choice = st.sidebar.selectbox("Select Main Menu", menu)

    if choice == "SVM":
        svm_sub_menu()
    elif choice == "Random Forest":
        rf_sub_menu()

def svm_sub_menu():
    st.subheader("SVM")

    # SVM submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
         os.system('streamlit run RF/Fish/app.py')
    elif choice == "Fruit":
         os.system('streamlit run RF/Fish/app.py')

def rf_sub_menu():
    st.subheader("Random Forest")

    # Random Forest submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
        os.system('streamlit run RF/Fish/app.py')
    elif choice == "Fruit":
        os.system('streamlit run RF/Fish/app.py')

if __name__ == "__main__":
    main()
