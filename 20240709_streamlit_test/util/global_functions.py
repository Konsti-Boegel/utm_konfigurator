import streamlit as st

import time

def create(url, channel, channel_group, budget, format, project):
    return 1

def reset():
    return 1

def show_warning(missing_parameters):
    missing_parameters_str = ', '.join(missing_parameters)  # Wandelt die Liste in einen String um, mit Kommas getrennt
    st.warning('Fehlende Angaben: ' + missing_parameters_str)

def check_null(parameters):
    while True:
        null_parameters = []
        for i in parameters:
            if i=='':
                null_parameters.append(i)
        return null_parameters
    time.sleep(1)