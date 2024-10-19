FROM python:3.9-slim

WORKDIR /home/data

COPY scripts.py /home/data/scripts.py
COPY IF.txt /home/data/IF.txt
COPY AlwaysRememberUsThisWay.txt /home/data/AlwaysRememberUsThisWay.txt

RUN mkdir -p /home/data/output

CMD ["python", "/home/data/scripts.py"]