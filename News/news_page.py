"""
This code designs the Home Page
"""
import streamlit as st
from .news import news

def news_page():
	tab1,tab2,tab3 = st.tabs(["2023","2022","2021"])
	style = """<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">"""

	with tab1:
		for j,p in enumerate(news['2023']):
			st.markdown(style+p+"""</p>""", unsafe_allow_html=True)
	with tab2:
		for j,p in enumerate(news['2022']):
			st.markdown(style+p+"""</p>""", unsafe_allow_html=True)
	with tab3:
		for j,p in enumerate(news['2021']):
			st.markdown(style+p+"""</p>""", unsafe_allow_html=True)