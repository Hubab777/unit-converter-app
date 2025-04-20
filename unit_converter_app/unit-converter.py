import streamlit as st

st.title("Unit Converter App")
st.markdown("### Instant Converter for Length, Weight and Time")
st.write("Welcome! Choose a category, enter the value and get real-time converted result")

category = st.selectbox("Select any category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometres to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometres":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
    elif unit == "Pounds to Kilograms":
        return value / 2.20462
    
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60 
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        
if category == "Length":
    unit = st.selectbox("Select Conversion",["Kilometres to Miles", "Miles to Kilometres"])
        
elif category == "Weight":
    unit = st.selectbox("Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
    
elif category == "Time":
    unit = st.selectbox("Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
    
value = st.number_input("Enter the value")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
