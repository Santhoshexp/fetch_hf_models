FROM python:alpine

RUN  pip install pandas &&  pip install huggingface_hub

ADD test.py .


ENTRYPOINT  [ "python" ,'main.py' ]