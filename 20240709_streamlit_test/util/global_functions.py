import streamlit as st

import time

def create(url, channel, channel_group, budget, format, project):
    return 1

def reset():
    return 1

# Funktion zur Anzeige der Warnung
def show_warning(missing_parameters):
    null_params = check_null(missing_parameters)
    if null_params:
        st.warning(f'Fehlende Angaben: {", ".join(null_params)}')

def check_null(parameters):
    null_parameters = []
    for key, value in parameters.items():
        if value == '':
            null_parameters.append(key)
    return null_parameters