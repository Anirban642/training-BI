
import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3:latest")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "my_collection")

# Initialize embedding model
def get_embeddings():
    return OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url=OLLAMA_BASE_URL
    )


# Connect to existing Qdrant collection
def get_vector_store():
    return QdrantVectorStore.from_existing_collection(
        embedding=get_embeddings(),
        collection_name=COLLECTION_NAME,
        url=QDRANT_URL
    )


# Initialize local LLM
def get_llm():
    return OllamaLLM(
        model=LLM_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0
    )


# Retrieve relevant chunks
def retrieve_documents(question):
    vector_store = get_vector_store()
    results = vector_store.similarity_search(
        query=question,
        k=4
    )
    return results


# Generate answer using retrieved context
def generate_answer(question):
    documents = retrieve_documents(question)

    if not documents:
        return "No relevant information found in the knowledge base."

    context = "\n\n".join(
        document.page_content for document in documents
    )

    prompt = f"""You are a helpful document assistant.

Answer the user's question using only the information
provided in the context.

Rules:
1. Answer questions about any type of document.
2. Do not assume the document is of a particular type. It can be anything, such as a PDF, Word document, or text file.
3. Do not invent information.
4. If the answer is unavailable, clearly say that
   the provided documents do not contain the answer.
5. Give a clear and relevant answer.

Context:
{context}

Question:
{question}

Answer:"""

    llm = get_llm()
    return llm.invoke(prompt)


# Terminal chat
def chat():
    print("\n========== DOCUMENT RAG CHAT ==========")
    print("Ask questions about your documents.")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() in ["exit", "quit", "bye"]:
            print("Chat ended.")
            break

        if not question:
            continue

        try:
            answer = generate_answer(question)
            print("\nAssistant:", answer)

        except Exception as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    chat()
