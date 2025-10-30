# Use PyTorch base image
FROM pytorch/pytorch:2.1.0-cpu

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask==2.3.3 transformers==4.36.0 sentencepiece==0.1.99 protobuf==3.20.0

EXPOSE 5000

CMD ["python", "app.py"]


