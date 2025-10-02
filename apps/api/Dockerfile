FROM python:3.11-slim

WORKDIR /code

# system deps (if needed)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# minimal deps
RUN pip install --no-cache-dir fastapi uvicorn[standard] 

# copy app
COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

