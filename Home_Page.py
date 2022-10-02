import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title='Home Page', page_icon='☀️', layout='wide')
st.title('Solar Flare Prediction with Deep Learning')
st.markdown(
    '<h5>The <i>Carrington Event</i> of 1859 was the most intense solar event of the century. During this, '
    'a series of powerful coronal mass ejections hit Earth. The resulting effects were observed worldwide and '
    'observations of glowing night sky auroras were recorded. This space weather event caused geomagnetic currents in '
    'long stretches of the telegraph transmission lines that were common in that day, generating enough current for '
    'the lines to operate without batteries. There were no high voltage (HV) electrical power transmission lines back '
    'then, so, the impact of the Carrington Event on global safety and economics was minor.',
    unsafe_allow_html=True)
st.markdown(
    '<h5>In today\'s world,where nearly everything relies on electricity and computers and machines powered by the '
    '“grid,” such an event would be Fatal. Solar storms can eject large amounts of high energy particles as solar '
    'wind, and when these winds reach Earth, they can damage telecommunications satellites, power lines, '
    'and other electrical or electronic systems. The HV power lines and substations we depend on could potentially be '
    'damaged or put out of commission for months or years, since lead time to obtain such large power transformers is '
    'very long and they are expensive items to replace.',
    unsafe_allow_html=True)
st.markdown(
    '<h5> DSCOVR sits at the Sun-Earth L1 Lagrange point about one million miles away from Earth, and can warn us '
    'about 45 minutes in advance of a space weather event. DSCOVR uses a variety of instruments to detect solar '
    'activity and flares. One critical DSCOVR instrument in use since 2015 is the Faraday Cup (FC), which tracks the '
    'peak solar wind speed. However,the faraday cup is also detecting noise and the readings were affected due to '
    'this.',
    unsafe_allow_html=True)
st.markdown(
    '<h5> The dataset used in this project comes from the following paper: <a '
    'href="https://www.sciencedirect.com/science/article/pii/S235234092100487X">Data set for solar flare prediction '
    'using HMI vector magnetic field data</a>',
    unsafe_allow_html=True)

with open('final_analysis.html', 'rb') as f:
    buf = BytesIO(f.read())
st.download_button('Click here to view the analysis of the dataset', buf, file_name='HMI_data_summary.html')

names = ['FLARE_NUMBER', 'T_REC', 'NOAA_AR', 'QUALITY', 'LONGITUDE', 'LATITUDE', 'TOTUSJH',
         'TOTBSQ', 'TOTPOT', 'TOTUSJZ', 'ABSNJZH', 'SAVNCPP', 'USFLUX', 'AREA_ACR', 'TOTFZ', 'MEANPOT', 'R_VALUE',
         'EPSZ', 'SHRGT45', 'MEANSHR', 'MEANGAM', 'MEANGBT', 'MEANGBZ', 'MEANGBH', 'MEANJZH', 'TOTFY', 'MEANJZD',
         'MEANALP', 'TOTFX', 'EPSY', 'EPSX']

info = [
        'Refers to data from the GOES Event representing whether a flare occurred or not. Attribute\'s values labeled as 1 are related to M- or X-class flare events. On the other hand, when their values equal 0, they are related to A-, B-, or C-class events, or no event.',
        'Contains date and time that the magnetic data were collected from SHARP.',
        'Shows the number of the active region where the event occurred (where the magnetic data were taken from).',
        'This attribute refers to a flag from the SHARP\'s data set showing whether records are noisy (This attribute holds values from a pre-defined table as disposed in [10]). When errors occur during the SHARP\'s data processing, the quality attribute reports them by holding values higher than 65,536 (or 10,000 in hexadecimal) [1,3,4,8]. If attribute\'s values range between 0 and 65,536, their associated data are of good quality. Each value corresponds to a distinct type of error that may occur while processing satellite\'s data.',
        'This attribute was obtained from the SRS data set aiming to perform a filter on the active regions that were outside a defined radius from the central meridian [1,4,9]. This attribute shows the longitude in which the active region can be encountered in the solar surface.',
        'This attribute contains the latitude at which the active region can be found on the solar surface.',
        'Total unsigned current helicity. This attribute and all the twenty four following attributes are the data from the Spaceweather HMI Active Region Patch (SHARP) data sets provided by the JSOC. They correspond to magnetic measurements and physical parameters derived from active regions that were automatically tracked by the HMI equipment. Details about those attributes can be found in Bobra [4].',
        'Total magnitude of Lorentz force.',
        'Total photospheric magnetic free energy density.',
        'Total unsigned vertical current.',
        'Absolute value of the net current helicity.',
        'Sum of the absolute value of the net current per polarity.',
        'Total unsigned flux.',
        'Area of strong field pixels in the active region.',
        'Sum of z-component of Lorentz force.',
        'Mean photospheric magnetic free energy.',
        'Sum of flux near polarity inversion line.',
        'Sum of z-component of normalized Lorentz force.',
        'Fraction of Area with shear >45°.',
        'Mean shear angle',
        'Mean angle of field from radial',
        'Mean gradient of total field',
        'Mean gradient of vertical field',
        'Mean gradient of horizontal field',
        'Mean current helicity (Bz contribution)',
        'Sum of y-component of Lorentz force',
        'Mean vertical current density',
        'Mean characteristic twist parameter, α',
        'Sum of x-component of Lorentz force',
        'Sum of y-component of normalized Lorentz force',
        'Sum of x-component of normalized Lorentz force'
        ]
info_table = pd.DataFrame()
info_table['Attribute\'s Name'] = names
info_table['Description'] = info
info_table.set_index('Attribute\'s Name')
st.subheader('Detailed description of attributes of the dataset is shown below')
st.table(info_table)
