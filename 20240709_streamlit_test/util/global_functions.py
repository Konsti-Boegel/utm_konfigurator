import streamlit as st

def create(url, channel, channel_group, budget, format, project):
    return 1

def reset():
    return 1

def show_warning(missing_parameters):
    missing_parameters_str = ', '.join(missing_parameters)  # Wandelt die Liste in einen String um, mit Kommas getrennt
    st.warning('Fehlende Angaben:' + missing_parameters_str)