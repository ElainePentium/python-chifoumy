# app/Dockerfile   -> app = test_steph

FROM python:3.10.6

EXPOSE 8501

WORKDIR /test_steph

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/* \
    python3-opencv


# RUN git clone https://github.com/streamlit/streamlit-example.git .

RUN pip install opencv-python

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
