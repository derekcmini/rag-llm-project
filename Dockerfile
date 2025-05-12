FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    cmake \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN git clone https://github.com/ggerganov/llama.cpp.git
WORKDIR /app/llama.cpp
RUN make -j$(nproc)

WORKDIR /app
CMD ["python", "scripts/api_server.py"]
