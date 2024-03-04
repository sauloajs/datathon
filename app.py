import streamlit as st
from src.layouts.reset_styles import *
from src.layouts.navbar import *

st.set_page_config(layout="wide", page_title="Educação - Futuro e Presente", page_icon=":notebook:")

resetStyles()

nav = getNavBarHtml()

st.markdown(nav, unsafe_allow_html=True)

# <style>
#     .css-1avcm0n {
#         display: none !important;
#     }

#     div.block-container {
#         padding: 0 !important;
#     }

#     header:nth-child(1) {
#         display: none !important;
#     }

#     .e1akgbir11 {
#         display: none !important;
#     }
# </style>