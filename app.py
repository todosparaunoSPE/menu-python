# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:04:08 2024

@author: jperezr
"""

import streamlit as st

st.title("CONCENTRADO")
st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")



with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Estudio ubicación de CAP's", "https://mapa-censo-inegi-2020-cap-huff-4nidjfue7kpqkgab5vkc9w.streamlit.app/")
        with col2:
           st.link_button("Base de datos IRN", "https://irn-base-cq6rxr3tlwucktlgxycpiy.streamlit.app/")
        
           
           
           