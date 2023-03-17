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



st.header('EXOPLANETAS - DONDE ESTAN TODOS 👽?')
st.write('\n')


#st.write('Tenemos 5309 planetas descubiertos. Sabemos de uno, que obtiene vida. ya esta?')

milkyway = Image.open('Screenshot 2023-03-16 at 20.45.08.png')
st.image(milkyway, caption='Milky Way')

st.subheader('QUE HACE EL MACHINE LEARNING EN ESTE CASO? ')


# insert image
ml = Image.open('Screenshot 2023-03-17 at 02.23.28.png')
st.image(ml, caption='ml explained')

image = Image.open('Screenshot 2023-03-16 at 22.42.38.png')
st.image(image, caption='Exoplanetas')



