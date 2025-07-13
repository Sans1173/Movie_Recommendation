import pickle
import pandas as pd
import requests
import streamlit as st

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/' + str(movie_id) + '?api_key=<KEY>')
    data = response.json()
    return ""


def recommend(movie):
    movie_index =movies[movies['title']== movie].index[0]
    distances = similarity[movie_index]
    movie_list= sorted(list(enumerate(distances)), reverse= True, key = lambda x:x[1])[1:6]

    recommended_movies =[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movie_dict =pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Netflix Recommending')
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

