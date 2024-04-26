FROM python:3.11

WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .

ARG DB_URL
ENV DB_URL=$DB_URL

CMD ["uvicorn", "app.main:app", "--port=8000", "--host=0.0.0.0"]