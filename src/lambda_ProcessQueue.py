import os
import json
import boto3
from decimal import Decimal
from sns_client import publish_notification  # <--- import novo

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ.get("ADS_TABLE")

def lambda_handler(event, context):
    """
    Lambda acionada pela SQS.
    - Lê mensagens da fila.
    - Insere os anúncios no DynamoDB.
    - Publica notificação no SNS.
    """
    table = dynamodb.Table(TABLE_NAME)

    for record in event.get("Records", []):
        try:
            # Lê a mensagem da fila
            message = json.loads(record["body"])
            anuncio = message.get("payload", {})

            # Insere no DynamoDB
            table.put_item(
                Item={
                    "anuncio_id": anuncio["anuncio_id"],
                    "usuario": anuncio["usuario"],
                    "marca": anuncio["marca"],
                    "modelo": anuncio["modelo"],
                    "preco": Decimal(str(anuncio["preco"])),
                    "estado": anuncio.get("estado", "disponível")
                }
            )

            print(f"✅ Anúncio {anuncio['anuncio_id']} inserido com sucesso!")

            # Publica notificação no SNS
            notification = {
                "titulo": "Anúncio criado com sucesso!",
                "anuncio_id": anuncio["anuncio_id"],
                "marca": anuncio["marca"],
                "modelo": anuncio["modelo"],
                "preco": anuncio["preco"],
                "usuario": anuncio["usuario"]
            }

            publish_notification(notification, subject="Confirmação de anúncio")

        except Exception as e:
            print(f"❌ Erro ao processar mensagem: {e}")

    return {"status": "ok"}
    