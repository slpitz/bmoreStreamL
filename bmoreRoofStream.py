# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:27:53 2020

@author: Scott
"""

import streamlit as st

#to make things easier later, also import...
import numpy as np
import pandas as pd

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.image('CITY-LOGO.png', caption="Charm City", width=100)

st.title('Project Skylight')

DATE_COLUMN = 'date/time'
DATA_URL = ('Vacant_Buildings_lat_long.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 1000 rows of data into the dataframe.
data = load_data(4000)
# Notify the reader that the data was successfully loaded.
st.write('Done! (using st.cache)')

st.subheader('Raw data')
st.write(data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

# st.map(map_data)
st.map(data)