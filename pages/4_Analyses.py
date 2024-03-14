import streamlit as st
from src.layouts.styles import *
from src.layouts.navbar import *
from src.layouts.pages.analyses import *
from src.graphs.analyses import *

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

container = st.container()

max_column_width = 650

with container:
    st.markdown(getHeader(), unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        getEngagementWorldCloud(2020)
        st.markdown(f'<style>div.stFrame {{ max-width: {max_column_width}px; }}</style>', unsafe_allow_html=True)
    
    with col2:
        getEngagementWorldCloud(2022)
        st.markdown(f'<style>div.stFrame {{ max-width: {max_column_width}px; }}</style>', unsafe_allow_html=True)