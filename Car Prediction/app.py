import streamlit as st
import time

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

sidebar = st.sidebar

sidebar.title("Sidebar Title Here")
btn1 = sidebar.button("Get Snow")

if btn1:
    st.snow()

st.title("Car Price Prediction")
name = st.text_input("Enter Car model")
btn = st.button("Submit")
Address = st.text_input("Enter Total Miles that car is running")

btn2 = st.button("Click")

if btn:
    st.text(f"You entered name {name}")

if btn2:
    st.text(f"My Address is{Address}")


st.image('car.jpg', use_column_width=True)