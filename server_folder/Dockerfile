FROM python:3.10-slim

COPY . /streamlit_ollama_server_app
WORKDIR /streamlit_ollama_server_app

RUN apt-get update && apt-get install -y curl build-essential

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -qU langchain-groq

EXPOSE 5000
#  --no-cache-dir
CMD ["python", "server.py"]
