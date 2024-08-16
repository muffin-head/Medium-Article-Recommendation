import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
vectorizer=joblib.load('app/models/tfidf_vectorizer.pkl')
article_vectors=joblib.load('app/models/train_article_vectors.pkl')
article_df=pd.read_csv('app/data/medium_data.csv')
def get_recommendation(user_input,top_n=3):
    user_vector=vectorizer.transform([user_input])
    sim_score= cosine_similarity(user_vector,article_vectors).flatten()
    top_indices=sim_score.argsort()[-top_n:][::-1]
    top_articles=article_df.iloc[top_indices]
    return top_articles[['title','publication','url']]

