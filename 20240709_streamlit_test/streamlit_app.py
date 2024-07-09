import os
import sys
import threading
import time

current_dir = os.getcwd()
sys.path.insert(0, current_dir)

import streamlit as st

from util.budget_utils import *
from util.channel_utils import *
from util.channel_group_utils import *
from util.format_utils import *
from util.project_utils import *
from util.global_functions import *
from util.global_utils import *


st.write("""
# UTM Konfigurator (Web-Version)
UTM-Link Erstellung
""")


# Text-Input für URL
user_url = st.text_input('Landingpage-URL eingeben:')
# Selectbox für Kanäle
user_channel = st.selectbox('Kanal', sorted(set(get_channels())))
# Selectbox für Kanalgruppen
user_channel_group = st.selectbox('Kanalgruppe', sorted(set(get_channel_group())))
# Radio für Werbebudget
user_budget = st.radio('Werbebudget', get_budget())
# Selectbox für Formate
user_format = st.selectbox('Format', sorted(set(get_format())))
# Selectbox für Projekte
user_project = st.selectbox('Projekt', sorted(set(get_project())))


param_dict = {'URL': user_url,
              'Kanal': user_channel,
              'Kanalgruppe': user_channel_group,
              'Werbebudget': user_budget,
              'Format': user_format,
              'Projekt': user_project}


# Starte den Thread für die Warnung
warning_thread = threading.Thread(target=show_warning(param_dict))
warning_thread.start()


# Button für Link-Erstellung
#st.button('Link erstellen', on_click=create(param_dict))
# Button für Reset
st.button('Reset')


# streamlit run 20240709_streamlit_test/streamlit_app.py