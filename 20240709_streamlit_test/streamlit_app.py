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
from util.absender_utils import *
from util.interest_utils import *

tab1, tab2 = st.tabs(["UTM-Konfigurator", "FAQ"])

with tab1:
    st.write("""
    # UTM Konfigurator (Web-Version)
    ##### 
    ### Pflichtfelder
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
    # Selectbox für Absender
    user_absender = st.selectbox('Absender', sorted(set(get_absender())))


    st.write("""
    ##### 
    
    ### Optionale Parameter
     
     
    """)

    # Selectbox für Interesse
    user_interest = st.selectbox('Interesse', sorted(set(get_interest())))


    param_dict = {'URL': user_url,
                  'Kanal': user_channel,
                  'Kanalgruppe': user_channel_group,
                  'Werbebudget': user_budget,
                  'Format': user_format,
                  'Projekt': user_project,
                  'Absender': user_absender}

    opt_param_dict = {'Interesse': user_interest}

    def get_param_dict():
        return {'URL': user_url,
                'Kanal': user_channel,
                'Kanalgruppe': user_channel_group,
                'Werbebudget': user_budget,
                'Format': user_format,
                'Projekt': user_project,
                'Absender': user_absender}

    def get_opt_param_dict():
        return {'Interesse': user_interest}


    # Starte den Thread für die Warnung
    warning_thread = threading.Thread(target=show_warning(get_param_dict()))
    warning_thread.start()


    # Button für Link-Erstellung
    if st.button('Link erstellen'):
        create(get_param_dict(), get_opt_param_dict())


    # Button für Reset
    if st.button('Reset'):
        st.experimental_rerun()


# streamlit run 20240709_streamlit_test/streamlit_app.py