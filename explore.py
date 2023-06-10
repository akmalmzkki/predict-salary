import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public_preprocessing.csv")
    return df

df = load_data()

def show_explore_page():
    st.title("Eksplorasi penggajian")
    
    opsi1 = [
        'Country',
        'YearsCodePro',
        'EdLevel',
        'Employment',
    ]
    
    pilihan1 = st.selectbox("Pilih atribut untuk menghitung opsi yang dipilih berdasarkan salary", opsi1)
    

    if st.button("Tampilkan data"):
        st.divider()
        st.write(f"""Total penggajian berdasarkan {pilihan1} dengan Salary""")
        data = df.groupby([pilihan1])['Salary'].sum().sort_values(ascending=True)
        st.bar_chart(data)
    
    st.divider()
    
    opsi2 = [
        'Australia', 
        'Brazil', 
        'Canada',
        'France',
        'Germany',
        'India',
        'Italy',
        'Netherlands',
        'Other',
        'Poland',
        'Spain',
        'Sweden',
        'United Kingdom of Great Britain and Northern Ireland',
        'United States of America'
    ]
    
    pilihan2 = st.selectbox("Pilih negara untuk menghitung opsi yang dipilih berdasarkan salary", opsi2)
    
    if st.button("Tampilkan data"):
        st.divider()
        st.write(f"""Total penggajian berdasarkan {pilihan2} dengan Salary""")
        # Tampilkan scatterplot dengan negara yang dipilih sebagai sumbu x dan salary sebagai sumbu y
        data = df[df['Country'] == pilihan2]
        plt.scatter(data['Country'], data['Salary'])
        plt.xlabel('Country')
        plt.ylabel('Salary')
        plt.title('Total penggajian berdasarkan negara')
        st.pyplot()
        