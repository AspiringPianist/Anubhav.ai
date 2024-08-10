import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_together import Together
import os
from dotenv import load_dotenv

from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

together_api_key = "fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
model = None

# Load environment variables
load_dotenv()

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)

def query_rag(query_text: str, chat_id: str):
    global model
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=os.path.join(CHROMA_PATH, chat_id), embedding_function=embedding_function)

    # Search the DB.
    results = db.max_marginal_relevance_search(query_text, k=4)
    # use with scores
    #context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    context_text = "\n\n---\n\n".join([doc.page_content for doc in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # Initialize the Together AI model
    if not model:
        model = model = Together(
model="meta-llama/Meta-Llama-3-70B-Instruct-Lite",
temperature=0.7,
max_tokens=1024,
top_k=50,
together_api_key=together_api_key
)
    response_text = model.invoke(prompt)
    #use with _scores
    #sources = [doc.metadata.get("id", None) for doc, _score in results]
    sources = [doc.metadata.get("id", None) for doc in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text, sources

if __name__ == "__main__":
    main()