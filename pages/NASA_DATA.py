import streamlit as st
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
from PIL import Image


st.header('LA BASE DE DATOS DE NASA - SIN MACHINE LEARNING 🧠') 

nasa_data = pd.read_csv('HABITABILITY_NASA.csv')
nasa_data = nasa_data.drop(['Unnamed: 0'], axis=1)
nasa_data = nasa_data.drop(['Unnamed: 0.1'], axis=1)
nasa_data = nasa_data[['planet_name', 'planet_radius', 'planet_mass', 'eccentricity', 'habitability']]
nasa_data = nasa_data.dropna()
st.dataframe(nasa_data)

