"""
This code designs the Publication Page
"""
import streamlit as st
import numpy as np
from .publications import publications
from .publications import working_papers
from .scholar import n_citations

def publication_page():
	style = """<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">"""
	tab1, tab2 = st.tabs(["Published", "Work in progress"])
	with tab1:
		# Published
		tabs = st.tabs(['ALL'] + list(publications.keys()))
		with tabs[0]:
			col1, col2, col_, col_ = st.columns(4)
			with col1:
				n_total = np.array([len(publications[year]) for year in publications]).sum()
				st.metric(label="Total publications", value=n_total)
			with col2:
				st.metric(label="Total citations", value=n_citations)
			for i,year in enumerate(publications.keys()):
				st.subheader(year)
				for j,p in enumerate(publications[year]):
					rank = """<b>%s. </b>"""%(j+1)
					st.markdown(style+rank+p+"""</p>""", unsafe_allow_html=True)

		for i,year in enumerate(publications.keys()):
			with tabs[i+1]:
				for j,p in enumerate(publications[year]):
					rank = """<b>%s. </b>"""%(j+1)
					st.markdown(style+rank+p+"""</p>""", unsafe_allow_html=True)
	with tab2:
		# Working in progress
		for j,p in enumerate(working_papers):
			rank = """<b>%s. </b>"""%(j+1)
			st.markdown(style+rank+p+"""</p>""", unsafe_allow_html=True)
	