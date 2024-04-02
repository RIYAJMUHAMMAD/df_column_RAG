from src.retriever import VectorDBRetriever
from src.data_uploader import Store
# sentence transformers
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import dotenv_values
config = dotenv_values(".env")

embed_model = HuggingFaceEmbedding(model_name=config.get("MODEL_NAME"), max_length= int(config.get("MAX_TOKEN")))

vector_store = PGVectorStore.from_params(
            database=config.get("DB_NAME"),
            host=config.get("HOST"),
            password=config.get("PASSWORD"),
            port=config.get("PORT"),
            user=config.get("USER"),
            table_name=config.get("TABLE"),
            embed_dim=int(config.get("EMBED_DIM")),  # openai embedding dimension
        )
        
retriever = VectorDBRetriever(vector_store = vector_store, embed_model= embed_model, query_mode= "default" ,similarity_top_k= 3)
query = "hi"
retriever._retrieve(query)