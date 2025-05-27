import streamlit as st


# Função para criar o quadro estilizado
def big_number_card(title, value,color="#000000"):
    st.markdown(f"""
    <div style='
        width: 80%;
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
        <h3 style='margin-bottom:5px; color: {color}; font-size: 15px'>{title}</h3>
        <h2 style='margin:0; color: {color}; font-size: 30px'>{value}</h2>
    </div>
""", unsafe_allow_html=True)