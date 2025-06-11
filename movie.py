import streamlit as st
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


st.set_page_config(page_title="🎬 Movie Mood Matcher", layout="wide")

# Styling 
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: white;
        }
        .movie-card {
            background-color: rgba(30, 30, 30, 0.95);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            margin-bottom: 25px;
        }
        .movie-title {
            font-size: 22px;
            color: #f9a826;
            font-weight: bold;
        }
        .movie-overview {
            font-size: 16px;
            color: #ddd;
        }
        .genre-chip {
            display: inline-block;
            background-color: #333;
            padding: 5px 10px;
            border-radius: 15px;
            margin: 5px 5px 0 0;
            font-size: 13px;
            color: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

# Load Data
@st.cache_data
def load_data():
    embeddings = np.load(r"C:\Users\arjun\Movie recommendation system\notebook\movie_embeddings.npy")
    metadata = pd.read_parquet(r"C:\Users\arjun\Movie recommendation system\notebook\movie_metadata.parquet")
    return embeddings, metadata

movie_embeddings, metadata_df = load_data()

# Load Embedding Model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

#  Corpus Prep 
metadata_df['corpus'] = (
    metadata_df['title'].fillna('') + " " +
    metadata_df['overview'].fillna('')
)

#  Recommendation Function 
def recommend_movies_by_query(query, model, embeddings, metadata, top_n=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = similarities.argsort()[-top_n:][::-1]
    results = metadata.iloc[top_indices].copy()
    results['similarity'] = similarities[top_indices]
    return results[['title', 'overview', 'similarity'] + (['genres'] if 'genres' in results.columns else [])]

#  UI 
st.markdown("<h1 style='color:#f9a826;'>🎬 Movie Mood Matcher</h1>", unsafe_allow_html=True)
st.markdown("<p>Tell us what kind of movie you're in the mood for and get AI-powered recommendations!</p>", unsafe_allow_html=True)

query = st.text_input(
    "📝 Describe the mood, genre, or story you're interested in:",
    placeholder="e.g., A funny romantic movie set in high school"
)

if query:
    with st.spinner("🔍 Finding recommendations..."):
        recommendations = recommend_movies_by_query(query, model, movie_embeddings, metadata_df)
        st.markdown("### 🎯 Top Matches for You:")
        for _, row in recommendations.iterrows():
            st.markdown(f"""
                <div class="movie-card">
                    <div class="movie-title">{row['title']}</div>
                    <div class="movie-overview">{row['overview']}</div>
            """, unsafe_allow_html=True)

            if 'genres' in row and pd.notnull(row['genres']):
                genres = row['genres']
                if isinstance(genres, str):
                    genres = genres.split(',')
                genre_html = ''.join([f'<span class="genre-chip">{g.strip()}</span>' for g in genres])
                st.markdown(genre_html, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)
