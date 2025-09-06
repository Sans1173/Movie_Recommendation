# Movie Recommendation System

A content-based movie recommendation system using machine learning and Streamlit.
<img width="812" height="608" alt="image" src="https://github.com/user-attachments/assets/2fcb3652-43f3-4f05-bc0e-c2b3a91fdd00" />


## Features
- Recommends movies based on genres, keywords, cast, crew, and plot
- Interactive web interface with Streamlit
- Movie poster integration via TMDB API
- 5000+ movies dataset
## How It Works
1. Preprocesses movie data (genres, cast, keywords, overview)
2. Creates feature vectors using CountVectorizer
3. Calculates cosine similarity between movies
4. Recommends top 5 similar movies
## Installation
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
pip install pandas numpy scikit-learn nltk streamlit requests
## Usage
1. Select a movie from dropdown
2. Click "Recommend" 
3. Get 5 similar movie suggestions
## Files
- `movie_recommend_netflix.ipynb` - Data preprocessing
- `app.py` - Streamlit web app
- `movies.pkl` - Processed movie data
- `similarity.pkl` - Similarity matrix
## Dataset
TMDB 5000 Movie Dataset with movie details and credits information.
## Dependencies
- pandas, numpy, scikit-learn
- nltk, streamlit, requests
