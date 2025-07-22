from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders.csv_loader import CSVLoader


from dotenv import load_dotenv
load_dotenv()

class AnimeVectorStore:
    def __init__(self, csv_path:str, persist_directory:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_directory = persist_directory
        self.embedings = HuggingFaceEmbeddings(model = "all-MiniLM-L6-v2")
        

    def build_and_save_vectorstore(self):
        loader = CSVLoader(file_path=self.csv_path, encoding='utf-8',metadata_columns=[])
        data = loader.load()

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = splitter.split_documents(data)

        db = Chroma.from_documents(texts, self.embedings, persist_directory=self.persist_directory)
        db.persist()

    def load_vectorstore(self):
        return Chroma(persist_directory=self.persist_directory, embedding_function=self.embedings)
