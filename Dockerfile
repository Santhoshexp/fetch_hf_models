FROM python:alpine

RUN  pip install pandas &&  pip install huggingface_hub

ADD main.py .


ENTRYPOINT  [ "python" ,'main.py' ]
