from src.data_loader import AnimeDataLoader
from src.vector_store import AnimeVectorStore
from dotenv import load_dotenv
load_dotenv()
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the Anime Vector Store build process...")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed_csv= loader.load_and_process()

        logger.info("Data loaded and processed successfully.")
        vector_builder = AnimeVectorStore(
            csv_path=processed_csv,
            persist_directory="chroma_db"
        )
        vector_builder.build_and_save_vectorstore()
        logger.info("Vector store built and saved successfully.")   
    except Exception as e:
        logger.error(f"Error in building Anime Vector Store: {str(e)}")
        raise CustomException("Failed to build Anime Vector Store", e)  
    

if __name__ == "__main__":
    main()
    logger.info("Anime Vector Store build process completed.")
    print("Anime Vector Store build process completed successfully.")