import streamlit as st

from budget_utils import *
from channel_utils import *
from channel_group_utils import *
from format_utils import *
from project_utils import *
from global_functions import *
from global_utils import *
from format_utils import *

def run_form():
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

    return {'URL': user_url,
            'Kanal': user_channel,
            'Kanalgruppe': user_channel_group,
            'Werbebudget': user_budget,
            'Format': user_format,
            'Projekt': user_project}

