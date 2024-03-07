import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from src.layouts.styles import *
from src.layouts.navbar import *
from src.layouts.pages.educational_context import *
from src.graphs.line_graphs import plot_educational_expenses_graph

st.set_page_config(layout="wide", page_title="Educação - Contexto Educacional", page_icon=":notebook:")

resetStyles()

st.markdown("""
<style>
* {
    section.main {
        background: url('https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/bg-b1.png');
        background-attachment: fixed;
        background-position: bottom;
        background-repeat: no-repeat;
        background-size: cover;
        height: 100vh;
        overflow: hidden;
    }
}
</style>        
<script>
window.addEventListener('scroll', function() {
    let offset = window.pageYOffset;
    document.querySelector('section').style.backgroundPositionY = offset * 0.7 + 'px';
});
</script>    
""", unsafe_allow_html=True)

nav = getNavBarHtml('{educational-context-active}')
main = getMainSectionContent()
comments = getCommentsSectionContent()

st.markdown(nav, unsafe_allow_html=True)
st.markdown(main, unsafe_allow_html=True)

container = st.container()

with container:
    fig = plot_educational_expenses_graph()
    
st.markdown(comments, unsafe_allow_html=True)