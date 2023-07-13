import streamlit as st

sidebar = st.sidebar

sidebar.title("Sidebar Title Here")
btn1 = sidebar.button("Get Balloons")

if btn1:
    st.balloons()

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