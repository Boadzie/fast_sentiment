FROM python:3.9-slim

WORKDIR /api


COPY ./requirements.txt /api/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt


COPY . /api

CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8000"]
