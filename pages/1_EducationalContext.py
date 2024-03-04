import streamlit as st
from src.layouts.styles import *
from src.layouts.navbar import *
from src.layouts.pages.educational_context import *

st.set_page_config(layout="wide", page_title="Educação - Contexto Educacional", page_icon=":notebook:")

resetStyles()

st.markdown("""
<style>
* {
    section.main {
        background: url('https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/bg-1.png');
        background-size: cover;
        height: 100% !important;
    }
}
</style>            
""", unsafe_allow_html=True)

nav = getNavBarHtml('{educational-context-active}')
content = getPageContent()

st.markdown(nav, unsafe_allow_html=True)
st.markdown(content, unsafe_allow_html=True)