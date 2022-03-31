import streamlit as st
import streamlit.components.v1 as components
import os
from pylocator.positionstackfuns import latlonpositionstack

if "latitude" not in st.session_state.keys():
    st.session_state["latitude"] = 49.750
if "longitude" not in st.session_state.keys():
    st.session_state["longitude"] = 6.166
if "cityname" not in st.session_state.keys():
    st.session_state["cityname"] = "Luxembourg"

st.title("Weather Map using Streamlit")

st.markdown("""
    Welcome to this weather map. To use this application, simply select the input 
    type, which can be either the **city name** or the **latitude and longitude** 
    of the place that you want, then click the **Search** button. The map 
    will then change and show the weather of the place.
""")

st.markdown("---")

selectope = st.selectbox("Select input type", ["City name", "Latitude and Longitude"])

with st.form(key="location_input"):
    if selectope == "City name":
        locat = st.text_input("Type the city name below", value="Luxembourg")
    elif selectope == "Latitude and Longitude":
        latinput = st.number_input("Latitude",value=49.750)
        loninput = st.number_input("Longitude", value=6.166)
    subbutton = st.form_submit_button("Search")

if subbutton:
    if selectope == "City name":

        # Get the latitude and longitude
        latdata, londata = latlonpositionstack(
            os.environ.get("apipositionstack"),
            locat)
        st.session_state["latitude"] = latdata
        st.session_state["longitude"] = londata

    elif selectope == "Latitude and Longitude":
        # Get the latitude and longitude
        st.session_state["latitude"] = latinput
        st.session_state["longitude"] = loninput

latc = st.session_state["latitude"]
lonc = st.session_state["longitude"]

components.iframe(src=f"https://embed.windy.com/embed2.html?lat={latc}&lon={lonc}&detailLat={latc}&detailLon={lonc}&width=650&height=450&zoom=5&level=surface&overlay=wind&product=ecmwf&menu=&message=&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=default&metricTemp=default&radarRange=-1",
    height=500)
