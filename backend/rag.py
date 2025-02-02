import os
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from lightrag.utils import EmbeddingFunc
from dotenv import load_dotenv

load_dotenv()

rag = LightRAG(working_dir="./db", 
                llm_model_func=gpt_4o_mini_complete, 
                embedding_func=EmbeddingFunc(
                    embedding_dim=1536,
                    max_token_size=8192,
                    func=lambda texts: openai_embed(texts, model="text-embedding-3-small")),
                    graph_storage="Neo4JStorage", 
                    log_level="DEBUG"
                )

with open("./db/sample.txt") as f:
    rag.insert(f.read())

setupprompt = """
    You are to generate a script for a short, 60 second educational video, based on the query question.
    Use only the information provided in the sources.
    Do not use outside knowledge to generate a response.
    Use a conversational tone, as if you were speaking to a friend.
"""

# Query the knowledge graph to generate a script
def query(question):
    return rag.query_with_separate_keyword_extraction(question, param=QueryParam(mode="local"), prompt=setupprompt)

# Ingest data into the knowledge graph
def ingest(filename):
    with open("../db/" + filename) as f:
        rag.insert(f.read())