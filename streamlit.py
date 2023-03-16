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


st.title('NASA EXOPLANETS - WHERE ARE THEY? ')

st.header('siurghfaier')
st.subheader('sfgs')
st.markdown('## sfgisdzf')
st.write('**texto normal**')

nasadata = pd.read_csv('REALdata.csv')

st.dataframe(nasadata)

st.sidebar.header('header')
st.sidebar.subheader('subheader')
st.sidebar.markdown('## markdown')
st.sidebar.write('**texto normal**')
