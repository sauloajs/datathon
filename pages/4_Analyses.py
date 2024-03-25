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
        st.markdown("""
            <img 
                src="https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/wc2020.png" 
                alt="Redução da população em favelas em 16 anos" 
                class="img-fluid" style="width: 650px; height: 455px"
            />
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <img 
                src="https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/wc2022.png" 
                alt="Redução da população em favelas em 16 anos" 
                class="img-fluid" style="width: 650px; height: 455px"
            />
        """, unsafe_allow_html=True)
        
        
with st.container():
    st.markdown(getSubHeader(), unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        getEngagementClustersGraph()
    
    with col2:
        getIegXIndeGraph()