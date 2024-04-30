import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[106.8410, -6.1574], zoom_start=16)
folium.Marker([106.8410, -6.1574], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
