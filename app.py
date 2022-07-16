import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(id):
	response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(id))
	data = response.json()
	return "https://image.tmdb.org/t/p/w500"+data['poster_path']


def recommend(movie_index):
    distances = similarity[movie_index]
    movies_sorted_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    posters = []
    for i in movies_sorted_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from API
        posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies,posters



movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Select a movie',
movies['title'].values)

ind= movies[movies['title'] == selected_movie_name].index[0]

mid = movies.iloc[ind].movie_id


with st.container():
    st.image(fetch_poster(mid),width=200)
    #st.text(mid)

if st.button('Recommend'):
    names,posters= recommend(ind)
    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
        
    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(names[5])
        st.image(posters[5])

    with col2:
        st.text(names[6])
        st.image(posters[6])

    with col3:
        st.text(names[7])
        st.image(posters[7])

    with col4:
        st.text(names[8])
        st.image(posters[8])

    with col5:
        st.text(names[9])
        st.image(posters[9])
     
   
     

    
    
        
        
        
        
        
        
