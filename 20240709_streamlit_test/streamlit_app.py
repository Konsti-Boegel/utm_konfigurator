import os
import sys

current_dir = os.getcwd()
sys.path.insert(0, current_dir)

import streamlit as st

from util.budget_utils import *
from util.channel_utils import *
from util.channel_group_utils import *
from util.format_utils import *
from util.project_utils import *

st.write("""
# UTM Konfigurator (Web-Version)
UTM-Link Erstellung
""")

# Text-Input für URL
user_url = st.text_input('Landingpage-URL eingeben:')
# Selectbox für Kanäle
st.selectbox('Kanal', get_channels())
# Selectbox für Kanalgruppen
st.selectbox('Kanalgruppe', get_channel_group())
# Radio für Werbebudget
st.radio('Werbebudget', get_budget())
# Selectbox für Formate
st.selectbox('Format', get_format())
# Selectbox für Projekte
st.selectbox('Projekt', get_project())


# Button für Link-Erstellung
st.button('Link erstellen')
# Button für Reset
st.button('Reset')


# streamlit run 20240709_streamlit_test/streamlit_app.py