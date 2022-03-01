 
import plotly.express as px
import numpy as np
import pandas as pd
import streamlit as st
# read csv and processe
LifeExp_vs_year = pd.read_csv("LifeExp_vs_Year")
LifeExp_vs_liver_deaht = pd.read_csv("LifeExp_vs_liver_death")
Gdp_vs_femaleH = pd.read_csv("GDP_vs_femaleinthehouse")

st.write("""
# Global Health Trend of Several Indicators between Male & Female across Continents
""")

example = LifeExp_vs_year.groupby(['Year','Indicator Name'])[['LifeExpectancy','Pop']].mean().reset_index()

# Indicator = st.radio("Indicator: ", ('Year', 'Number of Liver Cancer Death'))
st.write("""
### Example: Overall Average Life Expectancy VS Year between Male and Female 
""")
LifeExp_AVG_fig = px.scatter(example,x="Year", y="LifeExpectancy",
             size="Pop", color= "Indicator Name",symbol = "Indicator Name",
                 hover_name="Indicator Name", size_max=60)
st.plotly_chart(LifeExp_AVG_fig)

st.write("""
### Explore Life Expectancy Between Genders for a Specific Country
""")
Country = st.selectbox("Country: ",np.array(LifeExp_vs_year.country.unique()))
df = LifeExp_vs_year[LifeExp_vs_year["country"] == Country]
LifeExp_Year_figure = px.scatter(df,x="Year", y="LifeExpectancy",
	         size="Pop", color= "Indicator Name", symbol = "Region",
                 hover_name="country", log_x=True, size_max=60)
st.plotly_chart(LifeExp_Year_figure)

st.write("""
### Explore Life Expectancy Between Genders across regions
""")
gender_selection = ["All Genders","Population, female", "Population, male"]
region_selection = np.append(np.array(LifeExp_vs_year.Region.unique()), ["All Regions"])
Gender = st.selectbox("Gender: ", gender_selection)
Region = st.selectbox("Region:" , region_selection)
for i in gender_selection:
    if i == Gender:
        if i == "All Genders":
            df = LifeExp_vs_year
        else:
            df = LifeExp_vs_year[LifeExp_vs_year["Indicator Name"] == i]
        break
for j in region_selection:
    if j == Region:
        if j == "All Regions":
            df = LifeExp_vs_year
        else:
            df = df[df['Region'] == j]
        break
LifeExp_Year_figure = px.scatter(df, x="Year", y="LifeExpectancy",
                                     size="Pop", color="Region", symbol="Indicator Name",
                                     hover_name="country", log_x=True, size_max=60)
st.plotly_chart(LifeExp_Year_figure)





