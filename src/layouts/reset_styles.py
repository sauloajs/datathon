import streamlit as st

def resetStyles():
    st.markdown("""
    <head>
        <style>
            .esravye0 {
                gap: 0;
            }
            
            .css-1avcm0n {
                display: none !important;
            }

            div.block-container {
                padding: 0 !important;
            }

            header:nth-child(1) {
                display: none !important;
            }

            .e1akgbir11 {
                display: none !important;
            }
            
            section.main {
                background: url('https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/bg-main.png');
                background-size: cover;
            }
        </style>
    </head>            
    """, unsafe_allow_html=True)