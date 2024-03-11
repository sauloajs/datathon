import streamlit as st

def resetStyles(backgroundImage: str = 'https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/bg-main.png'):
    st.markdown("""
    <head>
        <style>
            [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
                padding-left: 0;
                padding-right: 0;
                text-align: center;
            }
            
            
            .svg-container {
                background: #fff!important; 
            }
        
            * {
                font-family: "Roboto", sans-serif;
                overflow-x: hidden;
                color: #000;
            }
            
            a {
                text-decoration: none!important;
            }
            
            a:hover {
                color: #ccc!important;
                transition: 0.3s;
            }
            
            .nav-link {
                border-bottom: 1px solid #f69e04!important;
            }
            
            .nav-link:hover {
                border-bottom: 1px solid #996204!important;
            }

            .esravye0 {
                gap: 0;
            }
            
            .css-1avcm0n {
                display: none !important;
            }

            div.block-container {
                padding: 0 !important;
                height: 100% !important;
            }

            header:nth-child(1) {
                display: none !important;
            }
            
            section:nth-child(1) {
                display: none !important;
            }

            .e1akgbir11 {
                display: none !important;
            }
            
            section.main {
                background: url('https://raw.githubusercontent.com/sauloajs/datathon/main/src/assets/images/bg-main.png');
                background-size: cover;
                height: 100% !important;
            }
            
            .icon--image {
                width: 6em;
                height: 6em;
            }
            
            .fixed--bottom {
                position: fixed;
                bottom: 1em;
                right: 1em;
                width: 100%;
                gap: 0.75em;
            }
            
            .link--active {
                opacity: 0.7 !important;
                border-bottom: 1px solid #996204!important;
            }
            
            .color--title {
                color: #f69e04!important;
            }
            
            .color--subtitle {
                color: #fff!important;
            }
            
            hr.line--light {
                color: #ccc!important;
                border-bottom: 1px solid #ccc;
                opacity: 0.7;
            }
            
            hr.line--orange {
                color: #f69e04!important;
                border-bottom: 1px solid #f69e04;
                opacity: 0.7;
            }
        </style>
    </head>            
    """, unsafe_allow_html=True)