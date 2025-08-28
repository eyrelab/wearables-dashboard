import streamlit as st
import os
import re
import pandas as pd

st.title('overview')

dfs=[]
fileNames=[]
directory='/Users/ldimitrov/Downloads/wearables-dashboard-main/data_for_analysis'

for file in os.scandir(directory):
    fileNames.append(re.sub('[^0-9]','',file.name))#regex strip strings of non num values, patient ids?
    dfs.append(pd.read_csv(directory+'/'+file.name))

patientSelect=st.selectbox(
    'select patient id',
    (fileNames),#*sort these
    index=None
)

try:
    num=fileNames.index(patientSelect)#index of the selected patient
    df=dfs[num]

    st.markdown('<center>patient id #'+patientSelect+'</center>',unsafe_allow_html=True)
    times=df['datetime']
    st.markdown('start: '+times[0])
    st.markdown('end: '+times.iloc[-1])
    st.markdown('row count: '+str(df.shape[0])+' (including NA rows)')####**includes NA rows(?)
    ###########***can't/how to(?) link to dashboard w/ provided patient id
except ValueError:
    print('select a patient to plot their data')
    st.markdown('<center><i>select a patient to see their overview</i></center>',unsafe_allow_html=True)

st.divider()
