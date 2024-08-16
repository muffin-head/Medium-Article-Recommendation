FROM python:3.11.9-slim-bullseye
WORKDIR /recommendation_medium
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python3","-m","flask","run","--host=0.0.0.0","--port=80"]
