import boto3
import pandas as pd
import os
from botocore.client import Config

# Configurações do MinIO (S3 Local)
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "admin")
SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "00000000")
BUCKET_NAME = "northwind"

def get_s3_client():
    return boto3.client(
        's3',
        endpoint_url=MINIO_ENDPOINT,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        config=Config(signature_version='s3v4'),
        region_name='us-east-1'
    )

def create_bucket_if_not_exists(s3_client):
    buckets = s3_client.list_buckets()
    if BUCKET_NAME not in [b['Name'] for b in buckets['Buckets']]:
        print(f"Criando bucket: {BUCKET_NAME}")
        s3_client.create_bucket(Bucket=BUCKET_NAME)

def upload_to_minio(file_path, object_name):
    s3 = get_s3_client()
    create_bucket_if_not_exists(s3)
    
    print(f"Fazendo upload de {file_path} para {BUCKET_NAME}/{object_name}")
    s3.upload_file(file_path, BUCKET_NAME, object_name)
    print("Upload concluído com sucesso!")

if __name__ == "__main__":
    # Caminho onde os arquivos devem estar (dentro do projeto)
    RAW_DATA_PATH = "./data/raw"
    
    if not os.path.exists(RAW_DATA_PATH):
        os.makedirs(RAW_DATA_PATH)
        print(f"⚠️ Pasta {RAW_DATA_PATH} criada. Por favor, coloque os arquivos CSV nela.")
    else:
        # Tenta subir todos os arquivos CSV encontrados na pasta
        for file in os.listdir(RAW_DATA_PATH):
            if file.endswith(".csv"):
                upload_to_minio(os.path.join(RAW_DATA_PATH, file), file)
