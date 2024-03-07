import streamlit as st
from src.layouts.styles import *
from src.layouts.navbar import *
from src.layouts.pages.target_city import *
from src.graphs.line_graphs import plot_salaries_graph, plot_age_distortion_graph
from src.graphs.bar_graphs import plotEducationalDistGraph, plotSchoolsAdm, plotMatSPGraph, plotMatBRGraph, plotMatEmGraph

st.set_page_config(layout="wide", page_title="Educação - Embu Guaçu", page_icon=":notebook:")

resetStyles()

st.markdown("""
<style>
* {
    section.main {
        background: url('https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/bg-bb-3.jpg');
        background-size: cover;
        height: 100% !important;
    }
}
</style>            
""", unsafe_allow_html=True)

nav = getNavBarHtml('{target-city-active}')

st.markdown(nav, unsafe_allow_html=True)

container = st.container()

with container:
    st.markdown(getHeader(), unsafe_allow_html=True)
    
    tab1, tab2 = st.columns(2)
    
    with tab1: 
        plotEducationalDistGraph()
        
    with tab2:
        plot_salaries_graph()
    
    st.markdown(getSubHeader(), unsafe_allow_html=True)
    
    tab3, tab4 = st.columns(2)
    
    with tab3:
        plotSchoolsAdm()
    
    with tab4:
        plot_age_distortion_graph()
        
    st.markdown(getSubHeader2(), unsafe_allow_html=True)
    
    st.markdown(subtitle("Brasil: + 178,000"), unsafe_allow_html=True)
    plotMatBRGraph()
    
    st.markdown(subtitle("São Paulo (SP): + 30,000", True), unsafe_allow_html=True)
    plotMatSPGraph()
    
    st.markdown(subtitle("Embu-Guaçu: 61", True), unsafe_allow_html=True)
    plotMatEmGraph()