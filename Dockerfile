FROM python:3.9

WORKDIR /code

CMD 'python -m pip install --upgrade pip'
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY ./setup.py /code/setup.py
COPY ./src/app /code/src/app
COPY ./src/pairing/search /code/src/pairing/search
COPY ./src/pairing/model /code/src/pairing/model
COPY ./src/pairing/training /code/src/pairing/training
COPY ./src/pairing/utils /code/src/pairing/utils
COPY ./src/pairing/dataset/pairing/english.csv /code/src/pairing/dataset/pairing/english.csv
# RUN python /code/setup.py install
RUN pip install .
RUN pip freeze

COPY ./src/app /code/app

ENV PYTHONPATH /code
#docker run -p 8501:8501 mnemo_streamlit_gcp
CMD ["streamlit", "run", "app/streamlit_app.py"]
