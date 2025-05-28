import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Função para criar o quadro estilizado
def big_number_card(title, value,color="#000000"):
    st.markdown(f"""
    <div style='
        width: 100%;
        height: 50%;
        border: 2px solid {color};
        border-radius: 10px;
        padding: 5px;
        background-color: #C0C0C0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    '>
        <h3 style='margin-bottom:5px; color: {color}; font-size: 13px'>{title}</h3>
        <h2 style='margin:0; color: {color}; font-size: 25px'>{value}</h2>
    </div>
""", unsafe_allow_html=True)
    
def plotar_contagem(df, col):
    contagem = df[col].value_counts().head(5)
    plt.figure(figsize=(12,8))
    sns.barplot(x= contagem.index, y=contagem.values)
    plt.xlabel(col)
    plt.xticks(rotation=45)
    plt.show()

    