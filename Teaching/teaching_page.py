"""
This code designs the Teaching Page
"""
import streamlit as st
import pathlib
import os

def teaching_page():
	file_path = os.path.join(pathlib.Path(__file__).parent.resolve(),'files')
	col1,col2,col3 = st.columns(3)
	with col1:
		st.image(os.path.join(file_path,'course1.png'))
		st.header('Earth System Modeling: Basics and Applications')
		st.subheader('(地球系统模式基础与应用)')
		st.info("Graduate Course (2 credits) Fall 2022")
	with col2:
		st.image(os.path.join(file_path,'course2.png'))
		st.header('Spatio-Temporal Modeling and Analysis for Water Resources')
		st.subheader('(水资源时空模拟与分析)')
		st.info("Undergraduate Course (2 credits) Upcoming")
	with col3:
		st.image(os.path.join(file_path,'course3.png'))
		st.header('GIS/RS/GPS Field Study')
		st.subheader('(3S野外实习)')
		st.info("Undergraduate Course (1 credit) Co-taught in Summer 2021")
