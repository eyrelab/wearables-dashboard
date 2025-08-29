import streamlit as st
import pandas as pd
import os
import re
from datetime import datetime

st.title("wearables data dashboard")

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

meanMedSelect=st.selectbox(
    'select mean or median values',
    ('mean','median')
)

yData=st.radio(
    'pick data to plot',
    ['heart rate', 'respiratory rate', 'temperature', 'calibrated temperature'],
    #index=None
)

st.divider()

meanData={#link mean values
    'heart rate' : 'hr_mean',
    'respiratory rate' : 'rr_mean',
    'temperature' : 'temperature_mean',
    'calibrated temperature' : 'temperature_calib_mean'
}

medData={#link median values
    'heart rate' : 'hr_median',
    'respiratory rate' : 'rr_median',
    'temperature' : 'temperature_median',
    'calibrated temperature' : 'temperature_calib_median'
}

try:
    num=fileNames.index(patientSelect)#index of the selected patient
    df=dfs[num]

    st.markdown('<center>patient id #'+patientSelect+'</center>',unsafe_allow_html=True)

    if meanMedSelect=='mean':#probs a better way to do this
        st.line_chart(df,x='datetime',y=meanData[yData],x_label='time',y_label=yData,color="#89181A")
    elif meanMedSelect=='median':
        st.line_chart(df,x='datetime',y=medData[yData],x_label='time',y_label=yData,color="#89181A")
except ValueError:
    print('select a patient to plot their data')
    st.markdown('<center><i>select a patient to plot their data</i></center>',unsafe_allow_html=True)

st.divider()

st.subheader('num of devices worn at a time')#wont consider NA data as device was still worn?

#loop thru dfs and find min/max dates
minDate=min(dfs[0]['datetime'])#start with 1st and compare rest
maxDate=max(dfs[0]['datetime'])
for x in dfs:
    newMin=min(x['datetime'])
    newMax=max(x['datetime'])
    if newMin<minDate:
        minDate=newMin
    if newMax>maxDate:
        maxDate=newMax

#make a table with date range, loop thru each csv +
#check its min/max then +=1 to count column for all in range

dateRange=pd.date_range(minDate,maxDate,freq='5min')#records every 5mins
numWorn={
    'count':[0 for i in range(len(dateRange))]
}
dfWorn=pd.DataFrame(numWorn,index=[dateRange])

for x in dfs:
    dfMin=min(x['datetime'])
    dfMax=max(x['datetime'])
    dfWorn.loc[dfMin:dfMax]+=1#*SHOULD +1 to each count in between active dates?
    print(dfWorn.loc[dfMin])#the row at the minDate (loops so prints all 43)
    
st.line_chart(dfWorn, y='count')
st.dataframe(dfWorn)
print('hello')