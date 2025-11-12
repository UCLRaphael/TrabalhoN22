import os
import json
import boto3

sns = boto3.client("sns")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

def publish_notification(message: dict, subject: str = "Notificação de Anúncio"):
    """
    Publica uma mensagem no tópico SNS.
    """
    if not SNS_TOPIC_ARN:
        raise RuntimeError("Variável de ambiente SNS_TOPIC_ARN não configurada.")

    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=json.dumps(message),
        Subject=subject
    )

    print(f"📢 Mensagem publicada no SNS ({SNS_TOPIC_ARN}): {response['MessageId']}")
    return response
