FROM python:3

COPY ./server.py /

EXPOSE 9091
ENTRYPOINT ["python", "server.py"]
