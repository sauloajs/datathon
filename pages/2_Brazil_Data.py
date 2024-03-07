import streamlit as st
from src.layouts.styles import *
from src.layouts.navbar import *
from src.layouts.pages.brazil_data import *
from src.graphs.line_graphs import plot_poverty_rate_graph, plot_life_expectation_graph, plot_murder_rate_graph

st.set_page_config(layout="wide", page_title="Educação - Dados do Brasil", page_icon=":notebook:")

resetStyles()

st.markdown("""
<style>
* {
    section.main {
        background: url('https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/bg-br-b.png');
        background-size: cover;
        height: 100% !important;
        background-position: center;
    }
}
</style>            
""", unsafe_allow_html=True)

nav = getNavBarHtml('{brazil-data-active}')

st.markdown(nav, unsafe_allow_html=True)

container = st.container()

with container:
    st.markdown(getHeader(), unsafe_allow_html=True)
    
    col, col2 = st.columns(2)
    
    with col:
        plot_poverty_rate_graph()
    
    with col2:
        plot_life_expectation_graph()
        
    st.markdown(getSubHeader(), unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
            <img 
                src="https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/poverty_population.jpg" 
                alt="Redução da população em favelas em 16 anos" 
                class="img-fluid" style="width: 650px; height: 455px"
            />
        """, unsafe_allow_html=True)
    
    with col4:
        plot_murder_rate_graph()