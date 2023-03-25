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


st.write('Tenemos 5309 planetas conocidos. Esto son 0.000005% de los planetas que hay en nuestra galaxia.')
st.write('Sabemos de uno, que obtiene vida. Pero hay mas?')
st.write('\n')

milkyway = Image.open('Screenshot 2023-03-16 at 20.45.08.png')
st.image(milkyway,)


st.subheader('1. RELLENAR LA BASE DE DATOS DE NASA CON MACHINE LEARNING')


# insert image
ml = Image.open('Screenshot 2023-03-17 at 02.23.28.png')
st.image(ml, caption='ml explained')

image = Image.open('Screenshot 2023-03-16 at 22.42.38.png')
st.image(image, caption='Exoplanetas')

st.header('2. CALCULAMOS LA HABITABILIDAD DE CADA PLANETA')

euclidean = Image.open('Screenshot 2023-03-17 at 05.45.55.png')
st.image(euclidean, caption='Euclidean distances')


