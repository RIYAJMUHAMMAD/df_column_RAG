from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.postgres import PGVectorStore
from src.parser import Reader


class Store:

    def __initi__(self):

        self.vector_store = PGVectorStore.from_params(
            database=config.get("DB_NAME"),
            host=config.get("HOST"),
            password=config.get("PASSWORD"),
            port=config.get("PORT"),
            user=config.get("USER"),
            table_name=config.get("TABLE"),
            embed_dim=int(config.get("EMBED_DIM")),  # openai embedding dimension
        )

        self.reader = Reader()

    def upload(self, folder_path:str, sheet_name_is_influencial:bool, embed_model):
        nodes = self.reader._get_data(folder_path = folder_path, sheet_name_is_influencial= sheet_name_is_influencial)
        for node in nodes:
            node_embedding = embed_model.get_text_embedding(
                node.get_text()
            )
            node.embedding = node_embedding
        self.vector_store.add(nodes)