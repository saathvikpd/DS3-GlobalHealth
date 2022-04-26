import plotly.express as px
import numpy as np
import pandas as pd
import streamlit as st
import math
#read csv and processe
fm_year_avg = pd.read_csv("female_male_year copy.csv")
df_male_country = pd.read_csv("male_country copy.csv")

merged_final_pop = pd.read_csv("bmi_population_income.csv")
merged_year_avg = pd.read_csv("bmi_year_avg.csv")



# set up sidebar
a = st.sidebar
a.title("Indicators to Explore")
choice = a.radio("Navigation", ["LifeExpectancy", "Liver Cancer Death", "Lung Cancer Death", "Literacy", "Satisfaction", "%female in the house", "BMI and Income"])
# Setting up titles
st.write("""
# Global Health Trend of Several Indicators between Male & Female across Continents
""")
# if choice == "LifeExpectancy":
#     example = LifeExp_vs_year.groupby(['Year','Indicator Name'])[['LifeExpectancy','Pop']].mean().reset_index()

#     st.write("""
#     ### Example: Overall Average Life Expectancy VS Year between Male and Female 
#     """)
#     # the same way as you would draw in jupyter notebook
#     LifeExp_AVG_fig = px.scatter(example,x="Year", y="LifeExpectancy",
#                  size="Pop", color= "Indicator Name",symbol = "Indicator Name",
#                      hover_name="Indicator Name", size_max=60)
#     # streamlit function to dispaly plotly drawing. Check the correct function for matplotlib or others.
#     st.plotly_chart(LifeExp_AVG_fig)

#     # adding interactive selectbox so users can explore
#     st.write("""
#     ### Explore Life Expectancy Between Genders for a Specific Country
#     """)
#     Country = st.selectbox("Country: ",np.array(LifeExp_vs_year.country.unique()))
#     df = LifeExp_vs_year[LifeExp_vs_year["country"] == Country]
#     LifeExp_Year_figure = px.scatter(df,x="Year", y="LifeExpectancy",
#     	         size="Pop", color= "Indicator Name", symbol = "Region",
#                      hover_name="country", log_x=True, size_max=60)
#     st.plotly_chart(LifeExp_Year_figure)

#     st.write("""
#     ### Explore Life Expectancy Between Genders across regions
#     """)
#     gender_selection = ["All Genders","Population, female", "Population, male"]
#     region_selection = np.append(["All Regions"], np.array(LifeExp_vs_year.Region.unique()))
#     Gender = st.selectbox("Gender: ", gender_selection)
#     Region = st.selectbox("Region:" , region_selection)
#     for i in gender_selection:
#         if i == Gender:
#             if i == "All Genders":
#                 df = LifeExp_vs_year
#             else:
#                 df = LifeExp_vs_year[LifeExp_vs_year["Indicator Name"] == i]
#             break
#     for j in region_selection:
#         if j == Region:
#             if j == "All Regions":
#                 df = df
#             else:
#                 df = df[df['Region'] == j]
#             break
#     LifeExp_Year_figure = px.scatter(df, x="Year", y="LifeExpectancy",
#                                          size="Pop", color="Indicator Name", symbol="Country Name",
#                                          hover_name="country", log_x=True, size_max=60)
#     st.plotly_chart(LifeExp_Year_figure)

# if choice == "Liver Cancer Death":
#     st.write("""
#     ### Explore Life Expectancy VS Average Liver Cancer Death between Genders
#     """)
#     liver_lifeExp_avg = LifeExp_vs_liver_death.groupby(['Year','Indicator Name'])[['liver_death','LifeExpectancy','Pop']].mean().reset_index()
#     df = liver_lifeExp_avg

#     fig = px.scatter(df, x= "liver_death", y="LifeExpectancy",
#                  size="Pop", color= "Indicator Name",symbol = "Indicator Name",
#                      hover_name="Indicator Name", log_x=True, size_max=20)
#     st.plotly_chart(fig)


#     st.write("""
#     ### Explore Life Expectancy VS Liver Cancer Death between Gender for a specific country
#     """)

#     Country = st.selectbox("Country: ",np.array(LifeExp_vs_liver_death['Country Name'].unique()))

#     df = LifeExp_vs_liver_death[LifeExp_vs_liver_death['Country Name'] == Country]

#     fig = px.scatter(df,x="liver_death", y="LifeExpectancy",
#                  size="Pop", color= "Indicator Name", symbol = "Region",
#                      hover_name="Country Name", size_max=40, animation_frame = 'Year')
#     fig.update_layout(xaxis_range=(np.min(df['liver_death']), np.max(df['liver_death']) * 1.2 ),
#                      yaxis_range=(0, 100))
#     st.plotly_chart(fig)


#     st.write("""
#     ### Explore Life Expectancy VS Liver Cancer Death Between Genders across regions
#     """)
#     gender_selection = ["All Genders","Population, female", "Population, male"]
#     region_selection = np.append(["All Regions"], np.array(LifeExp_vs_liver_death.Region.unique()))
#     Gender_liver = st.selectbox("Gender : ", gender_selection)
#     Region_liver = st.selectbox("Region :" , region_selection)
#     for i in gender_selection:
#         if i == Gender_liver:
#             if i == "All Genders":
#                 df = LifeExp_vs_liver_death
#             else:
#                 df = LifeExp_vs_year[LifeExp_vs_year["Indicator Name"] == i]
#             break
#     for j in region_selection :
#         if j == Region_liver:
#             if j == "All Regions":
#                 df = df
#             else:
#                 df = df[df['Region'] == j]
#             break
#     fig = px.scatter(df,x="liver_death", y="LifeExpectancy",
#                  size="Pop", color= "Indicator Name", symbol = "Region",
#                      hover_name="Country Name", size_max=60, animation_frame ='Year')
#     fig.update_layout(xaxis_range=(np.min(df['liver_death'])*0.5, np.max(df['liver_death']) * 1.2 ),
#                      yaxis_range=(0, 100))

#     st.plotly_chart(fig)

# if choice == "Literacy":
#     example = LiteracyRate_vs_year.groupby(['Year','Indicator Name'])[['Lit','Pop']].mean().reset_index()

#     st.write("""
#     ### Example: Overall Average Literacy Rate by Subregion VS Year between Male and Female 
#     """)
#     # the same way as you would draw in jupyter notebook
#     LitRate_AVG_fig = px.scatter(example,x="Year", y="Lit",
#                  size="Pop", color= "Indicator Name",symbol = "Indicator Name",
#                      hover_name="Indicator Name", size_max=60)
#     # streamlit function to dispaly plotly drawing. Check the correct function for matplotlib or others.
#     st.plotly_chart(LitRate_AVG_fig)

#     # adding interactive selectbox so users can explore
#     st.write("""
#     ### Explore Literacy Rate Between Genders for a Specific Subregion
#     """)
#     Subregion = st.selectbox("Subregion: ",np.array(LiteracyRate_vs_year.Subregion.unique()))
#     df = LiteracyRate_vs_year[LiteracyRate_vs_year["Subregion"] == Subregion]
#     LitRate_Year_figure = px.scatter(df,x="Year", y="Lit",
#     	         size="Pop", color= "Indicator Name", symbol = "Subregion",
#                      hover_name="Subregion", log_x=True, size_max=20)
#     st.plotly_chart(LitRate_Year_figure)

#     st.write("""
#     ### Explore Literacy Rate Between Genders across subregions
#     """)
#     gender_selection = ["All Genders", "Population, female", "Population, male"]
#     Gender = st.selectbox("Gender: ", gender_selection)
#     for i in gender_selection:
#         if i == Gender:
#             if i == "All Genders":
#                 df = LiteracyRate_vs_year
#             else:
#                 df = LiteracyRate_vs_year[LiteracyRate_vs_year["Indicator Name"] == i]
#             break
#     LitRate_Year_figure = px.scatter(df, x="Year", y="Lit",
#                                          size="Pop", color="Indicator Name", symbol="Subregion",
#                                          hover_name="Subregion", log_x=True, size_max=60)
#     st.plotly_chart(LitRate_Year_figure)
    
# if choice == "Satisfaction":
#     example = SatRate_vs_year.groupby(['Year','Indicator Name'])[['Sat','Pop']].mean().reset_index()

#     st.write("""
#     ### Example: Overall Average Satisfaction Rate by Subregion VS Year between Male and Female 
#     """)
#     # the same way as you would draw in jupyter notebook
#     SatRate_AVG_fig = px.scatter(example,x="Year", y="Sat",
#                  size="Pop", color= "Indicator Name",symbol = "Indicator Name",
#                      hover_name="Indicator Name", size_max=60)
#     # streamlit function to dispaly plotly drawing. Check the correct function for matplotlib or others.
#     st.plotly_chart(SatRate_AVG_fig)

#     # adding interactive selectbox so users can explore
#     st.write("""
#     ### Explore Satisfaction Rate Between Genders for a Specific Subregion
#     """)
#     Subregion = st.selectbox("Subregion: ",np.array(LiteracyRate_vs_year.Subregion.unique()))
#     df = SatRate_vs_year[SatRate_vs_year["Subregion"] == Subregion]
#     SatRate_Year_figure = px.scatter(df,x="Year", y='Sat',
#     	         size="Pop", color= "Indicator Name", symbol = "Subregion",
#                      hover_name="Subregion", log_x=True, size_max=20)
#     st.plotly_chart(SatRate_Year_figure)

#     st.write("""
#     ### Explore Satisfaction Rate Between Genders across subregions
#     """)
#     gender_selection = ["All Genders", "Population, female", "Population, male"]
#     Gender = st.selectbox("Gender: ", gender_selection)
#     for i in gender_selection:
#         if i == Gender:
#             if i == "All Genders":
#                 df = SatRate_vs_year
#             else:
#                 df = SatRate_vs_year[SatRate_vs_year["Indicator Name"] == i]
#             break
#     SatRate_Year_figure = px.scatter(df, x="Year", y="Sat",
#                                          size="Pop", color="Indicator Name", symbol="Subregion",
#                                          hover_name="Subregion", log_x=True, size_max=60)
#     st.plotly_chart(SatRate_Year_figure)

if choice == "Lung Cancer Death": 
    example = fm_year_avg.groupby("year").mean().reset_index

    st.write("""
    ### Example: Overall Average death by year for females and males
    """)
    # the same way as you would draw in jupyter notebook
    male_female_deaths_fig = px.scatter(fm_year_avg, x = "year", y = fm_year_avg.columns[1:])
    male_female_deaths_fig.update_xaxes(tickangle = 45)
    # streamlit function to dispaly plotly drawing. Check the correct function for matplotlib or others.
    st.plotly_chart(male_female_deaths_fig)

    # countries and death 
    df_male_cancer_fig = px.bar(df_male_country, x = "country", y = "deaths")
    st.plotly_chart(df_male_cancer_fig)

    # top 10 countries with deaths --> males
    top_countries_male = df_male_country[:10]
    fig_top_male_lc = px.bar(top_countries_male, x = "country", y = "deaths")
    st.plotly_chart(fig_top_male_lc)
    

if choice == "BMI and Income": 
    
    st.write("""
    overall trend for BMI per country over years
    """)
    # the same way as you would draw in jupyter notebook
    df = merged_final_pop
    fig = px.scatter(df,x="income", y="BMI",
	         color= "gender", symbol = 'country', size='population',
                 hover_name='country', size_max=20, animation_frame = 'year')
    st.plotly_chart(fig)

    st.write("""
    Average BMI per year for females and males
    """)

    fig_year_avg = px.scatter(merged_year_avg, x = "year", y = merged_year_avg.columns[1:], title = 
                         "Average BMI per Year", labels={
                     "value": "BMI",
                 })
    fig_year_avg.update_xaxes(tickangle = 45)
    st.plotly_chart(fig_year_avg)

    # # adding interactive selectbox so users can explore
    # st.write("""
    # ### Explore Satisfaction Rate Between Genders for a Specific Subregion
    # """)
    # year = st.selectbox("Year: ",np.array(df["year"]))
    # df = df[Male_Female_lung_cancer["year"] == year]
    # male_female_deaths_fig = px.scatter(fm_year_avg, x = "year", y = fm_year_avg.columns[1:])
    # male_female_deaths_fig.update_xaxes(tickangle = 45)
    # st.plotly_chart(male_female_deaths_fig)





