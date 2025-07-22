import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Anime Recommendation System", page_icon=":sparkles:", layout="wide")

@st.cache_resource
def load_pipeline():
    return AnimeRecommendationPipeline()

pipeline = load_pipeline()

st.title("Anime Recommendation System")
query = st.text_input("Enter your favorite anime or genre eg.: light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you...."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations:")
        st.write(response)