import streamlit as st
import pandas as pd
import numpy as np
import base64

from streamlit_option_menu import option_menu
import streamlit_nested_layout

from Home import home_page
from Publications import publication_page
from Team import team_page
from Teaching import teaching_page
from Research import research_page

st.set_page_config(layout="wide")

def define_sidebar():
	with st.sidebar:
		select_sidebar = option_menu(None, ["Home", "Team",  "Research", 'Publications', 'Teaching','Presentations'], 
		    icons=['house', 'people', "gear", 'list-task', 'book','diagram-2-fill'], 
		    menu_icon="cast", default_index=0, orientation="vertical",
		    styles={
		        "container": {"padding": "0!important", "background-color": "#fafafa"},
		        "icon": {"color": "orange", "font-size": "25px"}, 
		        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
		        "nav-link-selected": {"background-color": "green"},
		    }
		)
	return select_sidebar

select_sidebar = define_sidebar()

if select_sidebar=="Home":
	home_page()

if select_sidebar=="Team":
	team_page()

if select_sidebar=="Publications":
	publication_page()

if select_sidebar=="Teaching":
	teaching_page()

if select_sidebar=="Research":
	research_page()


