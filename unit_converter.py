import streamlit as st

st.title("Unit Converter")

conversion_type = st.selectbox(
    "What would you like to convert?",
    [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Kilometers to Miles",
        "Miles to Kilometers",
        "Kilograms to Pounds",
        "Pounds to Kilograms"
    ]
)

value = st.number_input("Enter a value", value=0.0)


if st.button("Convert"):

    if conversion_type == "Celsius to Fahrenheit":
        result = (value * 9 / 5) + 32
        unit = "°F"

    elif conversion_type == "Fahrenheit to Celsius":
        result = (value - 32) * 5 / 9
        unit = "°C"

    elif conversion_type == "Kilometers to Miles":
        result = value * 0.621371
        unit = "miles"

    elif conversion_type == "Miles to Kilometers":
        result = value * 1.60934
        unit = "km"

    elif conversion_type == "Kilograms to Pounds":
        result = value * 2.20462
        unit = "lbs"

    elif conversion_type == "Pounds to Kilograms":
        result = value * 0.453592
        unit = "kg"

    st.success(f"{value} = {result:.2f} {unit}")