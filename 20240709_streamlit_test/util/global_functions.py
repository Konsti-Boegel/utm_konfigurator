import streamlit as st

def create(url, channel, channel_group, budget, format, project):
    return 1

def reset():
    return 1

missing_parameters = ['1', '2', '3']
def show_warning(missing_parameters):
    st.warning('Fehlende Angaben:' + missing_parameters)