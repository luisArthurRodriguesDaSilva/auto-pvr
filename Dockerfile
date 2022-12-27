FROM python:latest
COPY . /WD
RUN pip install tweepy && pip install numpy && pip install Pillow
WORKDIR /WD
CMD python scriptVersionAutoPvr.py