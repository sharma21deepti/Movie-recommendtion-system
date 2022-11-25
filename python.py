import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda s: s[1])[1:6]

    recommend_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
        # movies_id = movies.iloc[i[0]].movies_id
        # print(movies.iloc[i[0]].title)
    return recommend_movies,recommended_movies_poster


movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values
st.title('Movie Recommender System')
similarity = pickle.load(open('similarity.pkl', 'rb'))
selected_movie = st.selectbox('Enter movie name for recommendations', movies_list)

if st.button('Recommend'):
    recommend_movies,recommended_movies_poster = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_movies[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommend_movies[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommend_movies[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommend_movies[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommend_movies[4])
        st.image(recommended_movies_poster[4])
