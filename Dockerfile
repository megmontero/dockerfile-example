FROM python:3.9 
WORKDIR /app
COPY  src/ .
RUN ls -lstr .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
