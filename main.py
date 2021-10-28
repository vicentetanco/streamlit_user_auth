import streamlit as st
import time
import os
from SessionState import get



st.set_page_config(
    page_title="Name App",
    page_icon='icon.png',
    layout='wide')

session_state = get(passwtitlerd='')

if session_state.password != '':
    logo = st.empty()
    logo.image('logo.jpg',use_column_width= True)
    pwd_placeholder = st.empty()
    pwd = pwd_placeholder.text_input("Password:", value="", type="password")
    session_state.password = pwd
    if session_state.password == '':
        pwd_placeholder.empty()
        logo.empty()
        main()
    elif session_state.password != '':
        st.error("the password you entered is incorrect")
        with st.beta_expander("Olvide mi contraseña"):
            st.write('Please contact xx  :  mail')
else:
    main()

hide_streamlit_style = """ 
            <style> 
            #MainMenu {visibility: hidden;} 
            footer {visibility: hidden;} 
            </style> 
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
