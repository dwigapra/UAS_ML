import streamlit as st
import runpy

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
        # Add SVM Fish specific content or functionality here
    elif choice == "Fruit":
        st.write("You selected SVM -> Fruit.")
        # Add SVM Fruit specific content or functionality here

def rf_sub_menu():
    st.subheader("Random Forest Menu")

    # Random Forest submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
        st.write("You selected Random Forest -> Fish.")
        runpy.run_path('RF/Fish/app.py')
    elif choice == "Fruit":
        st.write("You selected Random Forest -> Fruit.")
        # Add Random Forest Fruit specific content or functionality here

if __name__ == "__main__":
    main()
