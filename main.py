import streamlit as st
import runpy

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
        # Add SVM Fish specific content or functionality here
    elif choice == "Fruit":
        # Add SVM Fruit specific content or functionality here

def rf_sub_menu():
    st.subheader("Random Forest")

    # Random Forest submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
        runpy.run_path('RF/app.py')
    elif choice == "Fruit":
        # Add Random Forest Fruit specific content or functionality here

if __name__ == "__main__":
    main()
