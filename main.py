import streamlit as st
from backend import get_data
import plotly.express as px

st.title("Weather Forecast for the next days")
place=st.text_input("place")
days= st.slider("forecast days",
                min_value=1,max_value=5,
                help="select the no of forecasted days")

option=st.selectbox("select data to view",
                    ("Temprature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")
if place:
    filtered_data=get_data(place, days)
    if option=="Temprature":
        tempratures=[dict["main"]["temp"]for dict in filtered_data]
        date=[dict["dt_txt"]for dict in filtered_data]
        #plotting map
        figure= px.line(x=date, y=tempratures, labels={"x":"date","y":"temprature(C)"})
        st.plotly_chart(figure)

    if option=="Sky":
        images={"Clear":"images/clear.png","Clouds":"images/cloud.png",
               "Rain":"images/rain.png","Snow":"images/snow.png"}
        sky_condition=[dict["weather"][0]["main"]for dict in filtered_data]
        image_paths=[images[condition] for condition in sky_condition ]
        print(sky_condition)
        st.image(image_paths, width=115)