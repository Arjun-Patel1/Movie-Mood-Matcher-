# Movie-Mood-Matcher-
🎬 Movie Mood Matcher 🎭
Find your perfect movie match—based on your mood!

Movie Mood Matcher is an AI-powered web app built with Streamlit that recommends movies based on how you feel or what kind of story you're in the mood for. Just describe your mood, and the app finds semantically similar movies using advanced Natural Language Processing (NLP) techniques.


🧠 How It Works
User types in a description like "A feel-good romantic movie with high school drama".

The app encodes this input using Sentence-BERT (MiniLM-L6-v2).

It compares the query against precomputed movie descriptions using cosine similarity.

Top 5 similar matches are returned with title, overview, and genres.

🖥️ Screenshots
<img src="https://your-placeholder.com/screenshot1.png" width="700"/> <img src="https://your-placeholder.com/screenshot2.png" width="700"/>
🛠️ Tech Stack
Component	Technology
Frontend	Streamlit (with custom CSS styling)
Embedding Model	SentenceTransformer (MiniLM-L6-v2)
Data	.parquet metadata + .npy embeddings
Language	Python
Similarity	Cosine similarity (scikit-learn)

📂 Files and Folders
bash
Copy
Edit
movie-mood-matcher/
├── movie.py                        # Main Streamlit app
├── movie_metadata.parquet         # Movie titles, overviews, genres
├── movie_embeddings.npy           # Precomputed SBERT embeddings
├── movie-mood-matchmaker-nlp.ipynb# Jupyter notebook for embedding creation
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
📦 Setup Instructions
1. Clone the Repository
2. Create Virtual Environment (Optional but Recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
streamlit run movie.py
📝 Sample Query
Input:
A mysterious, mind-bending sci-fi thriller with time travel

Output:

Interstellar

Inception

Predestination

Tenet

Donnie Darko

📈 Features
🔍 Natural language query for mood/genre/story

🎯 Top 5 relevant recommendations

🖼️ Beautiful, dark-themed UI with genre chips

🚀 Fast inference with cached resources and data

📌 To-Do / Improvements
🎥 Add poster images and trailers (TMDB API)

🎛️ Filter by year, genre, language

📱 Responsive layout for mobile

☁️ One-click deploy to Streamlit Cloud or HuggingFace Spaces

🤝 Contributing
Pull requests and feature ideas are welcome! Please open an issue or fork this project.

📜 License
This project is licensed under the MIT License.

📬 Contact
Developer: Arjun Patel
📧 Email: arjuinpatel89806@gmail.com
🔗 Linked in: www.linkedin.com/in/arjunpatel97259
