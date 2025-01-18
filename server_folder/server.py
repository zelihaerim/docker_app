from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
groq_api_key = os.environ['GROQ_API_KEY']

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)
#   docs_url="/docs"
# openai api
openai_model = ChatOpenAI()
# ollama model
ollama_model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

# Prompt Templates with embedded input variables
prompt1 = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant."),
    ("human", "Write me an essay about {topic} with 10 words")
    ])

prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

# Openai
add_routes(
    app,
    prompt1|openai_model,
    path="/openai/essay"
)
add_routes(
    app,
    prompt2|openai_model,
    path="/openai/poem"
)

# Ollama
add_routes(
    app,
    prompt1|ollama_model,
    path="/ollama/essay"
)
add_routes(
    app,
    prompt2|ollama_model,
    path="/ollama/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000) # host="localhost", port=8000
