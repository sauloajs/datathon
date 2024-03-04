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
                background: url('https://www.transparenttextures.com/patterns/brushed-alum-dark.png');
            }
        </style>
    </head>            
    """, unsafe_allow_html=True)