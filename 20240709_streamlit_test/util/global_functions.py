import streamlit as st
import random
import string

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
        utm_link = 'https://{url}?utm_source={channel}&utm_medium={budget}_{channel_group}&utm_content={format}_{absender}_{ID}&utm_campaign={project}'.format(
            url=param_dict.get('URL', 'NA'),
            channel=param_dict.get('Kanal', 'NA'),
            budget=param_dict.get('Werbebudget', 'NA'),
            channel_group=param_dict.get('Kanalgruppe', 'NA'),
            format=param_dict.get('Format', 'NA'),
            absender=param_dict.get('Absender', 'NA'),
            ID=generate_id(),
            project=param_dict.get('Projekt', 'NA')
        )
        st.success(f'Erstellter UTM-Link: {utm_link}')


def reset():
    return 1


def generate_id(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))