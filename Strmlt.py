import streamlit as st
import pandas as pd
import numpy as nm

##Title
st.title("Welcome to Maheshawari Institue")
##image
bg_img = r"C:\Users\Bhumika.barskar\OneDrive - Calsoft Pvt Ltd\Desktop\logo.png"
st.image(bg_img)

##simple text
st.write ('These are our packages.')
##DataFrame
df = pd.DataFrame({
    'Time':['One month', 'Two month','Three month','Six month','One year'],
    'Age': [1000, 1200, 1500, 2000,3000]
})
st.write(df)

##Taking input on strmlt
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}")

##Slider 
you_class = st.slider("Select your class:", 6,12)
st.write(f"You are in class {you_class}.")
 
##Select box
op = ['Maths', 'Science', 'Social', 'Chemistry', ' Physics']
ch = st.multiselect("Choose your preferred subject", op)
if ch:  # Check if the user selected any subjects
    if len(ch) == 1:
        st.write(f"You have selected {ch[0]} subject.")
    else:
        subjects = " and ".join(ch) if len(ch) == 2 else ", ".join(ch[:-1]) + f", and {ch[-1]}"
        st.write(f"You have selected {subjects} subjects.")
else:
    st.write("Please select at least one subject.")

