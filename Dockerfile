# TODO Add code for API container

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN echo # > ./__init__.py
COPY ./app/requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./app /app