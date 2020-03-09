FROM tensorflow/tensorflow:nightly

RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN pip install opencv-python flask werkzeug

COPY src ./src

WORKDIR /src

expose 8080

ENTRYPOINT ["python", "HttpConnectionSettings.py"]
