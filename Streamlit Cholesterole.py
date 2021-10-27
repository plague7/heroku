#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import plotly.express as px
import pandas as pd


# In[3]:



data=pd.read_csv("C:/Users/Simplon/Desktop/Travaux python/OpenFoodFacts - Cholesterole/dataNET_copie/data_cleaned.csv")

st.title('Cholesterôle')
st.plotly_chart(px.histogram(data, x="pnns_groups_2", 
                 color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending"))

