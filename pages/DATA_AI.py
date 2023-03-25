import Introduction as st
import streamlit as st
from PIL import Image  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import webbrowser as wb
import time
import os
from PIL import Image
import webbrowser
import base64
import io


pd.set_option('display.width', 10000)
st.header('LOS DATOS CON MACHINE LEARNING 🧠')

mydata = pd.read_csv('HABITABILITY_AI.csv')
mydata_free = pd.read_csv('HABITABILITY_AI.csv')
mydata = mydata.drop(['Unnamed: 0'], axis=1)
mydata = mydata.drop(['Unnamed: 0.1'], axis=1)
mydata = mydata[['planet_name', 'planet_radius', 'planet_mass', 'eccentricity', 'distances']]
mydata.rename(columns={'distances': 'habitability'}, inplace=True)
mydata = mydata.dropna()


# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(mydata)

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)
