FROM python:3.9

COPY /invoker.py /app/invoker.py
COPY /load_endpoints.py /app/load_endpoints.py
COPY /endpoint.py /app/endpoint.py
COPY /requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python", "/app/invoker.py"]
