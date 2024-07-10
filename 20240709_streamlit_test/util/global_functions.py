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
def create(param_dict, opt_param_dict):
    null_params = check_null(param_dict)
    if null_params:
        st.error(f'Fehlende Angaben: {", ".join(null_params)}')
    else:
        remove_empty_values(param_dict)
        remove_empty_values(opt_param_dict)
        utm_link = 'https://{url}?utm_source={channel}&utm_medium={budget}_{channel_group}&utm_content={format}_{absender}_{interest}_{ID}&utm_campaign={project}'.format(
            url=param_dict.get('URL', 'NA'),
            channel=param_dict.get('Kanal', 'NA'),
            budget=param_dict.get('Werbebudget', 'NA'),
            channel_group=param_dict.get('Kanalgruppe', 'NA'),
            format=param_dict.get('Format', 'NA'),
            absender=param_dict.get('Absender', 'NA'),
            interest=opt_param_dict.get('Interesse', 'NA'),
            ID=generate_id(),
            project=param_dict.get('Projekt', 'NA')
        ).lower()
        st.success(f'Erstellter UTM-Link: {utm_link}')


def reset():
    return 1


def generate_id(length=10):
    letters = string.ascii_letters
    digits = string.digits
    # Kombiniere die Buchstaben und Zahlen mit Wiederholung der Zahlen, um die Chancen auszugleichen
    characters = letters + digits * (len(letters) // len(digits))
    return ''.join(random.choice(characters) for _ in range(length))


def remove_empty_values(dict):
    return {key: value for key, value in dict.items() if value != ""}