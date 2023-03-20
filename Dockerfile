FROM python:3.8.10
COPY . /WD
RUN pip install --upgrade pip && pip install tweepy && pip install numpy && pip install Pillow && pip install python-dotenv
WORKDIR /WD
CMD python src/main.py