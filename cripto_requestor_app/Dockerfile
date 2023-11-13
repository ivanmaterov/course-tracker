FROM python:3.12

WORKDIR /app/

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
ENV PYTHONPATH=/app

ENTRYPOINT ["python", "-u", "main.py"]
