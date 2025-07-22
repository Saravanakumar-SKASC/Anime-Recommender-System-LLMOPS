from src.vector_store import AnimeVectorStore
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_directory="chroma_db"):
        try:
            logger.info("Initializing AnimeRecommendationPipeline...")

            vector_builder = AnimeVectorStore(
                csv_path="",
                persist_directory=persist_directory
            )
            retriever = vector_builder.load_vectorstore().as_retriever()

            self.recommender = AnimeRecommender(
                retriever=retriever,
                api_key=GROQ_API_KEY,
                model_name=MODEL_NAME
            )
            logger.info("AnimeRecommendationPipeline initialized successfully.")

        except Exception as e:
            logger.error(f"Error initializing AnimeRecommendationPipeline: {{str(e)}}")
            raise CustomException("Failed to initialize AnimeRecommendationPipeline", e)
        
    def recommend(self, query: str):
        try:
            logger.info(f"Received a query for recommendation: {query}")
            

            recommendation = self.recommender.get_recommendation(query)

            logger.info(f"Recommendation result: {recommendation}")
            return recommendation
        except Exception as e:
            logger.error(f"Error during recommendation: {str(e)}")
            raise CustomException("Failed to get recommendation", e)