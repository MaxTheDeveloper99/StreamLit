import streamlit as st

st.title("Temperature Converter")

st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")

# Enter temperature
temperature = st.number_input(
    "Enter temperature",
    value=0.0
)

# This is to choose a conversion to perform
conversion = st.selectbox(
    "Choose a conversion",
    [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Celsius to Kelvin",
        "Kelvin to Celsius"
    ]
)

# This is to perform a conversion
if conversion == "Celsius to Fahrenheit":
    result = (temperature * 9 / 5) + 32
    st.success(f"{temperature}°C = {result:.2f}°F")

elif conversion == "Fahrenheit to Celsius":
    result = (temperature - 32) * 5 / 9
    st.success(f"{temperature}°F = {result:.2f}°C")

elif conversion == "Celsius to Kelvin":
    result = temperature + 273.15
    st.success(f"{temperature}°C = {result:.2f} K")

elif conversion == "Kelvin to Celsius":
    result = temperature - 273.15
    st.success(f"{temperature} K = {result:.2f}°C")