import streamlit as st
from PIL import Image
import pandas as pd
from pytorch_tabnet.tab_model import TabNetClassifier
import numpy as np
import os
st.set_page_config(page_title='Model Interface', page_icon='🤖', layout='wide')
st.subheader('Feature Engineering')
img = Image.open('./pearson_correlation_matrix.JPG')
img1 = Image.open(
    './spearman_correlation_matrix.JPG')
col1, col2 = st.columns(2)
with col2:
    st.image(img.resize((480, 400)), caption='Pearson Correlation Matrix')
with col1:
    st.image(img1.resize((350, 350)), caption='Spearman Correlation Matrix')
st.markdown(
    '<h5> As can be seen from the Correlation matrices, Not all features are equally responsible for causing a major flare event. Due to this, we will consider only those features that have a high correlation with FlareNumber.',
    unsafe_allow_html=True)

st.subheader('Parameters - Time Series')
st.markdown(
        '<h5> Since the dataset has a record of solar flare activity for almost 10 years (May, 2010 to december, 2019), we can consider each parameter as a time series. So when we train a time series model on each parameter, the model will be able to predict the future values of the parameter.',
        unsafe_allow_html=True)
st.markdown(
        '<h5> This approach has been used for 3 parameters. The models were trained on data ranging from 2010 to 2017, and were able to predict values from 2018 to 2019.',
        unsafe_allow_html=True)

col1, col2= st.columns(2)
with col1: st.image(Image.open(
    './r_value_plot.png'))
with col2: st.image(Image.open(
    './MEANSHR_plot.png'))
st.image(Image.open(
    './SHRGT45_plot.png').resize((800,400)))

df = st.cache(pd.read_csv)('./SOLAR FLARE PREDICTION.csv', nrows=8500).reset_index()
st.subheader('Interactive model inference')
st.write(df)
selected = st.multiselect('Select rows', df.index)
selected = df.loc[selected]
run = st.checkbox('Run model')
st.write('### Selected Rows', selected)

if run:
    model = TabNetClassifier()
    model.load_model('pages/trained_models/SOLAR_FLARE_tabnet_classifier.zip')
    X = selected[['TOTUSJH', 'TOTBSQ', 'TOTPOT', 'TOTUSJZ','SAVNCPP', 'USFLUX', 'AREA_ACR', 'MEANPOT', 'R_VALUE',
                'SHRGT45', 'MEANSHR', 'TOTFY', 'TOTFX']]
    y = selected['FlareNumber']
    X = np.array(X)
    st.write('#### Model prediction', model.predict(X))

st.markdown(
        '<h6> This project uses the deep learning model, TabNet. Read more about <a href="https://arxiv.org/abs/1908.07442">TabNet</a>',
        unsafe_allow_html=True)
