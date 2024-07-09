import streamlit as st

import time

def create(url, channel, channel_group, budget, format, project):
    return 1

def reset():
    return 1

#def show_warning(missing_parameters):
#    missing_parameters_str = ', '.join(missing_parameters)  # Wandelt die Liste in einen String um, mit Kommas getrennt
#    st.warning('Fehlende Angaben: ' + missing_parameters_str)

# Funktion zur Anzeige der Warnung
def show_warning(missing_parameters):
    while True:
        null_params = check_null(missing_parameters)
        if null_params:
            st.warning(f'Fehlende Angaben: {", ".join(null_params)}')
        else:
            st.warning('')
        time.sleep(1)  # Aktualisiere die Warnung alle 1 Sekunde

def check_null(parameters):
    null_parameters = []
    for param in parameters:
        if param == '':
            null_parameters.append(param)
    return null_parameters