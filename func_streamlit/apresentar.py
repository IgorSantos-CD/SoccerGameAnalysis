import streamlit as st


# Função para criar o quadro estilizado
def big_number_card(title, value,color="#000000"):
    st.markdown(f"""
        <div style='
            width: 250px;
            height: 150px;
            border: 2px solid {color};
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            background-color: #05F0FF;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        '>
            <h4 style='margin-bottom:10px; color: {color}; font-size: 15px'>{title}</h4>
            <h2 style='margin:0; color: {color}; font-size: 30px''>{value}</h2>
        </div>
    """, unsafe_allow_html=True)