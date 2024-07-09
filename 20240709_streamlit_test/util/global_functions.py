import streamlit as st

import time
import sys

# Funktion zur Anzeige der Warnung
def show_warning(missing_parameters):
    null_params = check_null(missing_parameters)
    if null_params:
        st.warning(f'Fehlende Angaben: {", ".join(null_params)}')


# Funktion zur Suche nach leeren Parametern
def check_null(parameters):
    null_parameters = []
    for key, value in parameters.items():
        if value == '':
            null_parameters.append(key)
    return null_parameters



# Funktion zur Erstellung des UTM-Links
def create(param_dict):
    null_params = check_null(param_dict)
    if null_params:
        st.error(f'Fehlende Angaben: {", ".join(null_params)}')
    else:
        utm_link = 'https://{url}?utm_channel={channel}&utm_medium={channel_group}'.format(
            url=param_dict.get('URL', ''),
            channel=param_dict.get('Kanal', ''),
            channel_group=param_dict.get('Kanalgruppe', '')
        )
        st.success(f'Erstellter UTM-Link: {utm_link}')


def reset():
    return 1
