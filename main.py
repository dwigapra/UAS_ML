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
        if st.button("Run SVM -> Fish"):
            run_app('RF/Fish/app.py')
    elif choice == "Fruit":
        if st.button("Run SVM -> Fruit"):
            run_app('RF/Fish/app.py')

def rf_sub_menu():
    st.subheader("Random Forest")

    # Random Forest submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
        if st.button("Run Random Forest -> Fish"):
            run_app('RF/Fish/app.py')
    elif choice == "Fruit":
        if st.button("Run Random Forest -> Fruit"):
            run_app('RF/Fish/app.py')

def run_app(app_path):
    if os.path.exists(app_path):
        os.system(f'streamlit run {app_path}')
        st.success(f"Running: {app_path}")
    else:
        st.error(f"File not found: {app_path}")

if __name__ == "__main__":
    main()
