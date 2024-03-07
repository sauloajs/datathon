import streamlit as st
from src.layouts.styles import *
from src.layouts.navbar import *

st.set_page_config(layout="wide", page_title="Educação - Análises", page_icon=":notebook:")

resetStyles()

st.markdown("""
<style>
* {
    section.main {
        background: url('https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/bg-5.png');
        background-size: cover;
        height: 100% !important;
    }
}
</style>            
""", unsafe_allow_html=True)

nav = getNavBarHtml('{analyses-active}')

st.markdown(nav, unsafe_allow_html=True)