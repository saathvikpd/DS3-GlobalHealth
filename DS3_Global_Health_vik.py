import plotly.express as px
import numpy as np
import pandas as pd
import streamlit as st
import math
#read csv and processe
LifeExp_vs_year = pd.read_csv("LifeExp_vs_Year.csv")
LifeExp_vs_liver_death = pd.read_csv("LifeExp_vs_liver_death.csv")
Gdp_vs_femaleH = pd.read_csv("GDP_vs_femaleinthehouse.csv")
LiteracyRate_vs_year = pd.read_csv("literacy_v_year.csv")
SatRate_vs_year = pd.read_csv("satisfaction_v_year.csv")

# set up sidebar
a = st.sidebar
a.title("Indicators to Explore")
choice = a.radio("Navigation", ["LifeExpectancy", "Liver Cancer Death", "Lung Cancer Death", "Literacy", "Satisfaction", "%female in the house"])
# Setting up titles
st.write("""
# Global Health Trend of Several Indicators between Male & Female across Continents
""")
if choice == "LifeExpectancy":
    example = LifeExp_vs_year.groupby(['Year','Indicator Name'])[['LifeExpectancy','Pop']].mean().reset_index()

    st.write("""
    ### Example: Overall Average Life Expectancy VS Year between Male and Female 
    """)
    # the same way as you would draw in jupyter notebook
    LifeExp_AVG_fig = px.scatter(example,x="Year", y="LifeExpectancy",
                 size="Pop", color= "Indicator Name",symbol = "Indicator Name",
                     hover_name="Indicator Name", size_max=60)
    # streamlit function to dispaly plotly drawing. Check the correct function for matplotlib or others.
    st.plotly_chart(LifeExp_AVG_fig)

    # adding interactive selectbox so users can explore
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
    region_selection = np.append(["All Regions"], np.array(LifeExp_vs_year.Region.unique()))
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
                df = df
            else:
                df = df[df['Region'] == j]
            break
    LifeExp_Year_figure = px.scatter(df, x="Year", y="LifeExpectancy",
                                         size="Pop", color="Indicator Name", symbol="Country Name",
                                         hover_name="country", log_x=True, size_max=60)
    st.plotly_chart(LifeExp_Year_figure)

if choice == "Liver Cancer Death":
    st.write("""
    ### Explore Life Expectancy VS Average Liver Cancer Death between Genders
    """)
    liver_lifeExp_avg = LifeExp_vs_liver_death.groupby(['Year','Indicator Name'])[['liver_death','LifeExpectancy','Pop']].mean().reset_index()
    df = liver_lifeExp_avg

    fig = px.scatter(df, x= "liver_death", y="LifeExpectancy",
                 size="Pop", color= "Indicator Name",symbol = "Indicator Name",
                     hover_name="Indicator Name", log_x=True, size_max=20)
    st.plotly_chart(fig)


    st.write("""
    ### Explore Life Expectancy VS Liver Cancer Death between Gender for a specific country
    """)

    Country = st.selectbox("Country: ",np.array(LifeExp_vs_liver_death['Country Name'].unique()))

    df = LifeExp_vs_liver_death[LifeExp_vs_liver_death['Country Name'] == Country]

    fig = px.scatter(df,x="liver_death", y="LifeExpectancy",
                 size="Pop", color= "Indicator Name", symbol = "Region",
                     hover_name="Country Name", size_max=40, animation_frame = 'Year')
    fig.update_layout(xaxis_range=(np.min(df['liver_death']), np.max(df['liver_death']) * 1.2 ),
                     yaxis_range=(0, 100))
    st.plotly_chart(fig)


    st.write("""
    ### Explore Life Expectancy VS Liver Cancer Death Between Genders across regions
    """)
    gender_selection = ["All Genders","Population, female", "Population, male"]
    region_selection = np.append(["All Regions"], np.array(LifeExp_vs_liver_death.Region.unique()))
    Gender_liver = st.selectbox("Gender : ", gender_selection)
    Region_liver = st.selectbox("Region :" , region_selection)
    for i in gender_selection:
        if i == Gender_liver:
            if i == "All Genders":
                df = LifeExp_vs_liver_death
            else:
                df = LifeExp_vs_year[LifeExp_vs_year["Indicator Name"] == i]
            break
    for j in region_selection :
        if j == Region_liver:
            if j == "All Regions":
                df = df
            else:
                df = df[df['Region'] == j]
            break
    fig = px.scatter(df,x="liver_death", y="LifeExpectancy",
                 size="Pop", color= "Indicator Name", symbol = "Region",
                     hover_name="Country Name", size_max=60, animation_frame ='Year')
    fig.update_layout(xaxis_range=(np.min(df['liver_death'])*0.5, np.max(df['liver_death']) * 1.2 ),
                     yaxis_range=(0, 100))

    st.plotly_chart(fig)

if choice == "Literacy":
    example = LiteracyRate_vs_year.groupby(['Year','Indicator Name'])[['Lit','Pop']].mean().reset_index()

    st.write("""
    ### Example: Overall Average Literacy Rate by Subregion VS Year between Male and Female 
    """)
    # the same way as you would draw in jupyter notebook
    LitRate_AVG_fig = px.scatter(example,x="Year", y="Lit",
                 size="Pop", color= "Indicator Name",symbol = "Indicator Name",
                     hover_name="Indicator Name", size_max=60)
    # streamlit function to dispaly plotly drawing. Check the correct function for matplotlib or others.
    st.plotly_chart(LitRate_AVG_fig)

    # adding interactive selectbox so users can explore
    st.write("""
    ### Explore Literacy Rate Between Genders for a Specific Subregion
    """)
    Subregion = st.selectbox("Subregion: ",np.array(LiteracyRate_vs_year.Subregion.unique()))
    df = LiteracyRate_vs_year[LiteracyRate_vs_year["Subregion"] == Subregion]
    LitRate_Year_figure = px.scatter(df,x="Year", y="Lit",
    	         size="Pop", color= "Indicator Name", symbol = "Subregion",
                     hover_name="Subregion", log_x=True, size_max=20)
    st.plotly_chart(LitRate_Year_figure)

    st.write("""
    ### Explore Literacy Rate Between Genders across subregions
    """)
    gender_selection = ["All Genders", "Population, female", "Population, male"]
    Gender = st.selectbox("Gender: ", gender_selection)
    for i in gender_selection:
        if i == Gender:
            if i == "All Genders":
                df = LiteracyRate_vs_year
            else:
                df = LiteracyRate_vs_year[LiteracyRate_vs_year["Indicator Name"] == i]
            break
    LitRate_Year_figure = px.scatter(df, x="Year", y="Lit",
                                         size="Pop", color="Indicator Name", symbol="Subregion",
                                         hover_name="Subregion", log_x=True, size_max=60)
    st.plotly_chart(LitRate_Year_figure)
    
if choice == "Satisfaction":
    example = SatRate_vs_year.groupby(['Year','Indicator Name'])[['Sat','Pop']].mean().reset_index()

    st.write("""
    ### Example: Overall Average Satisfaction Rate by Subregion VS Year between Male and Female 
    """)
    # the same way as you would draw in jupyter notebook
    SatRate_AVG_fig = px.scatter(example,x="Year", y="Sat",
                 size="Pop", color= "Indicator Name",symbol = "Indicator Name",
                     hover_name="Indicator Name", size_max=60)
    # streamlit function to dispaly plotly drawing. Check the correct function for matplotlib or others.
    st.plotly_chart(SatRate_AVG_fig)

    # adding interactive selectbox so users can explore
    st.write("""
    ### Explore Satisfaction Rate Between Genders for a Specific Subregion
    """)
    Subregion = st.selectbox("Subregion: ",np.array(LiteracyRate_vs_year.Subregion.unique()))
    df = SatRate_vs_year[SatRate_vs_year["Subregion"] == Subregion]
    SatRate_Year_figure = px.scatter(df,x="Year", y='Sat',
    	         size="Pop", color= "Indicator Name", symbol = "Subregion",
                     hover_name="Subregion", log_x=True, size_max=20)
    st.plotly_chart(SatRate_Year_figure)

    st.write("""
    ### Explore Satisfaction Rate Between Genders across subregions
    """)
    gender_selection = ["All Genders", "Population, female", "Population, male"]
    Gender = st.selectbox("Gender: ", gender_selection)
    for i in gender_selection:
        if i == Gender:
            if i == "All Genders":
                df = SatRate_vs_year
            else:
                df = SatRate_vs_year[SatRate_vs_year["Indicator Name"] == i]
            break
    SatRate_Year_figure = px.scatter(df, x="Year", y="Sat",
                                         size="Pop", color="Indicator Name", symbol="Subregion",
                                         hover_name="Subregion", log_x=True, size_max=60)
    st.plotly_chart(SatRate_Year_figure)