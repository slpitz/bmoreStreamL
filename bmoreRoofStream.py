# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:27:53 2020

@author: Scott
"""

import streamlit as st
from os import listdir
from os.path import isfile, join
from PIL import Image

#to make things easier later, also import...
import numpy as np
import pandas as pd

#other libraries
import rasterio
from shapely.geometry import box
import geopandas as gpd
from fiona.crs import from_epsg

def getNeighbors(geoTiff, bigdf): #geotiff, dataframe to parse, new dataframeName
    """Function to show image of vacant property"""
    
    loadedGeotif = rasterio.open(geoTiff)
    #loadedGeotif.bounds
    #bounding box, assumes box is north south
    northlat = loadedGeotif.bounds[3]
    southlat = loadedGeotif.bounds[1]
    westLong = loadedGeotif.bounds[0]
    eastLong = loadedGeotif.bounds[2]
    
    newdf = bigdf[(bigdf['lat'] > southlat) & 
                            (bigdf['lat'] < northlat) &
                            (bigdf['lon'] < eastLong)&
                            (bigdf['lon'] > westLong)]
    return newdf
    #return df that has the addresses in the photo

def subsetVac(divisor):
    dataframe1 = pd.read_csv(DATA_URL)
    remain = list(range(1, len(dataframe1), divisor))
    filtered = dataframe1.iloc[remain]
    return filtered 

st.sidebar.image('CITY-LOGO.png', caption="Charm City", width=100)

testSetDataframe = pd.read_csv('testSetPreds.csv')

dropDownAddress = testSetDataframe[['dashAddress']]

st.write(dropDownAddress['dashAddress'].values.tolist())

onlyfiles = [f for f in listdir("AddressPhotos/") if isfile(join("AddressPhotos/", f))]
#st.write(type(onlyfiles))
imageselect = st.sidebar.selectbox("Pick an image.", dropDownAddress['dashAddress'].values.tolist())
st.write(onlyfiles)

#Contact Info
st.sidebar.markdown("""
### Contact 
This website was created by Scott Pitz (insert email).""")

st.title('Project Skylight')

DATE_COLUMN = 'date/time'
DATA_URL = ('Vacant_Buildings_lat_long.csv')

#st.title('Animal Identification')
st.write("Pick an image from the left. You'll be able to view the image.")
#st.write("When you're ready, submit a prediction on the left.")

image = Image.open("AddressPhotos/" + imageselect)
st.image(image, caption="Let's predict roof integrity.", width=300)

loadedGeotif = rasterio.open("AddressPhotos/" + imageselect)
#st.write(loadedGeotif.bounds)


#load shapefile deried csv
st.write("load real property file")
realPropShape1 = pd.read_csv('CondensedRealPropShapeData.csv')

#run function to produce
#st.write("show df of photo")
closeby = getNeighbors("AddressPhotos/" + imageselect, realPropShape1)
#st.write(closeby)

st.table(closeby)

DATE_COLUMN = 'date/time'
DATA_URL = ('Vacant_Buildings_lat_long.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

def subsetVac(divisor):
    dataframe1 = pd.read_csv(DATA_URL)
    remain = list(range(1, len(dataframe1), divisor))
    filtered = dataframe1.iloc[remain]
    return filtered 


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 1000 rows of data into the dataframe.
data = load_data(5000)
# Notify the reader that the data was successfully loaded.
st.write('Done! (using st.cache)')


st.subheader('Subset of current Vacant Homes')
smallerVacantdf = subsetVac(15)

#st.write('Subset of vacant homes from across Baltimore')
st.map(smallerVacantdf)
st.write(smallerVacantdf)

#To Do:
#select subset of vacant homes to show on map - done
#remove brackets and clean up drop down menu

