from src.data_uploader import Store
# sentence transformers
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import dotenv_values
config = dotenv_values(".env")

embed_model = HuggingFaceEmbedding(model_name=config.get("MODEL_NAME"), max_length=int(config.get("MAX_TOKEN")))
store = Store()
folder_path = "data"
store.upload(folder_path= folder_path, sheet_name_is_influencial=False, embed_model=embed_model)