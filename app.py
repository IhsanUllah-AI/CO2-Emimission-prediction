import streamlit as st
import requests
col1,col2,col3=st.columns(3)
x1=col1.number_input("Enter Engine Size b/w -0.55 and 6.9")
x2=col2.number_input("Enter Cylinders Number b/w 1 and 9.5")
x3=col3.number_input("Enter Fuel Consumption City b/w 3.35 and 20.6 ")

col4,col5=st.columns(2)
x4=col4.number_input("Enter Fuel Consumption Hwy b/w 3.45 and 14.4 ")
x5=col5.number_input("Enter Fuel Consumption Comb b/w 3.35 and 17.8")
url=f"http://127.0.0.1:8000/emmission/{x1}/{x2}/{x3}/{x4}/{x5}"

if st.button("predict CO2 Emmission"):
    st.write(f"URL constructed: {url}")
    response=requests.get(url)
    if response.status_code==200:
        st.info(response.json())

