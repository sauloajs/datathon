import streamlit as st
from src.layouts.styles import *
from src.layouts.navbar import *
from src.layouts.index import *

st.set_page_config(layout="wide", page_title="Educação - Futuro e Presente", page_icon=":notebook:")

resetStyles()

nav = getNavBarHtml('{index-active}')
content = getIndexHtml()

st.markdown(nav, unsafe_allow_html=True)
st.markdown(content, unsafe_allow_html=True)