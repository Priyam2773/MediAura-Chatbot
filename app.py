from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# ---------------------------------
# Flask App
# ---------------------------------

app = Flask(__name__)

# ---------------------------------
# Load Environment Variables
# ---------------------------------

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is missing.")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing.")

# ---------------------------------
# Embeddings
# ---------------------------------

embeddings = download_hugging_face_embeddings()

# ---------------------------------
# Pinecone
# ---------------------------------

index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# ---------------------------------
# Gemini Model
# ---------------------------------

chatModel = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.4
)

# ---------------------------------
# Prompt
# ---------------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(
    chatModel,
    prompt
)

rag_chain = create_retrieval_chain(
    retriever,
    question_answer_chain
)

# ---------------------------------
# Routes
# ---------------------------------

@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["POST"])
def chat():

    user_input = request.form.get("msg", "")

    if user_input.strip() == "":
        return "Please enter a question."

    response = rag_chain.invoke(
        {"input": user_input}
    )

    return response["answer"]


# ---------------------------------
# Run App
# ---------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)