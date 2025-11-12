import os
import json
import boto3

sqs = boto3.client("sqs")
QUEUE_URL = os.environ.get("QUEUE_URL")

def send_to_queue(message: dict):
    """
    Envia uma mensagem para a fila SQS.
    """
    if not QUEUE_URL:
        raise RuntimeError("Variável de ambiente QUEUE_URL não configurada.")
    
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message)
    )
    print(f"📤 Mensagem enviada para fila: {response['MessageId']}")
    return response
