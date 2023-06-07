"""
This code designs the Teaching Page
"""
import streamlit as st
import pathlib
import os

def research_page():
	file_path = os.path.join(pathlib.Path(__file__).parent.resolve(),'files')
	st.warning("""
		I study the geography of global inland waters 

I use hydrologic models at unprecedented spatial resolution, space observations, and data-driven methods to understand the fundamentals of surface water dynamics and its feedback to the climate system. 

My research takes a holistic earth system view to understand the global inland waters and its related fields. 
""")

	tab1, tab2, tab3 = st.tabs(["1. Modeling and remote sensing of the global river continuum", 
						"2. Flood mechanisms and forecasting",
						"3. Land-atmosphere interaction"])
	with tab1:
		col1,col2 = st.columns(2)
		with col1:
			st.image(os.path.join(file_path,'Picture1.png'))
			st.header('Reconstruction of naturalized river flows')
			st.info("Lin et al. (2019; WRR); this paper won the prestigious WRR Editor's Choice Award (given to 1% of papers annually)")
		with col2:
			st.image(os.path.join(file_path,'Picture2.png'))
			st.header('Bankfull river width')
			st.info("Lin et al. (2020; GRL)")
	with tab2:
		col1,col2 = st.columns(2)
		with col1:
			st.image(os.path.join(file_path,'Picture3.png'))
			st.header('Flood propagation speed influences flood peak')
			st.info("Lin et al. (2018; JHM)")
		with col2:
			st.image('https://github.com/geowaterpku/homepage/raw/main/animation.gif')
			st.header('Large-scale fine-resolution flood simulation')
			st.info("Lin et al. (2018a, JHM; 2018b, EMS; 2018c, JAWRA)")
	with tab3:
		col1,col2,col3 = st.columns(3)
		with col1:
			st.image(os.path.join(file_path,'Picture4.jpeg'))
			st.header('Snow hydrological/climatic effect')
		with col2:
			st.image(os.path.join(file_path,'Picture5.png'))
			st.header('Snow-temperature')
			st.info("""Lin et al. (2016; GRL)
			Media report at: https://www.sciencedaily.com/releases/2016/12/161206111455.htm
			""")
		with col3:
			st.image(os.path.join(file_path,'Picture6.png'))
			st.header('Snow-monsoon')
			st.info("""Lin et al. (2020; ERL)
			Media report at: https://www.sciencedaily.com/releases/2020/07/200716120705.htm
			""")

