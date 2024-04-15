import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/movies.csv")
movies_data.dropna()

#  sidebar_thanh bên    

with st.sidebar:
    st.sidebar.markdown("Select a range on the slider (it represents movie score) to view the total number of movies in a genre that falls within that range")
    new_score_rating = st.slider(label = "Choose a value:",
                                  min_value = 1.0,
                                  max_value = 10.0,
                                 value = (3.0,4.0))
    st.sidebar.markdown("Select your preferred genre(s) and year to view the movies released that year and on that genre")
    genre_list = movies_data['genre'].unique().tolist()
    new_genre_list = st.multiselect('Choose Genre:',
                                        genre_list, default = ['Animation', 'Horror', 'Fantasy', 'Romance'])
    
    st.sidebar.selectbox("Choose a Year",['1980','1981','1982','1983','1984','1895','1986','1987','1988','1989','1990','1991','1992','1993',
                          '1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',
                           '2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])
# main

st.write("""#### Interactive Dashboard """)
st.write("""####  Interact with this dashboard using the widgets on the sidebar""")

left_column, right_column = st.columns(2)
with left_column:
    st.write("""#### Lists of movies filtered by year and Genre """)
    genre = movies_data.genre
    year = movies_data.year
    a = movies_data.loc[(year == 1980)&((genre == 'Horror')|(genre == 'Animation')|(genre == 'Fantasy')), ['name', 'genre', 'year']]
    a=a.sort_values(by = 'name',ascending=True)
    ind = []
    for i in range(len(a.name)):
       ind.append(i)
    a.index=ind

    st.table(a)
    
with right_column:
    st.write("""#### User score of movies and their genre """)
    score_info = (movies_data['score'].between(*new_score_rating))
    rating_count_year = movies_data[score_info].groupby('genre')['score'].count()
    rating_count_year = rating_count_year.reset_index()
    figpx = px.line(rating_count_year, x = 'genre', y = 'score')
    st.plotly_chart(figpx)


    
st.markdown("Average Movie Budget, Grouped by Genre")
avg_budget = movies_data.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']
fig = plt.figure(figsize = (19, 10))
plt.bar(genre, avg_bud, color = 'maroon')
plt.xlabel('genre')
plt.ylabel('budget')
plt.title('Matplotlib Bar Chart Showing the Average Budget of Movies in Each Genre')
st.pyplot(fig)

    
