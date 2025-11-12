import json
from sqs_client import send_to_queue

def lambda_handler(event, context):
    """
    Lambda acionada pelo API Gateway.
    - Recebe o anúncio.
    - Envia a mensagem para a fila SQS (não grava diretamente no banco).
    """
    try:
        body = json.loads(event.get("body", "{}"))
        required = ["anuncio_id", "usuario", "marca", "modelo", "preco"]

        # Validação simples
        for campo in required:
            if campo not in body:
                return _response(400, {"erro": f"Campo obrigatório ausente: {campo}"})

        # Envia mensagem para a fila
        message = {
            "type": "novo_anuncio",
            "payload": body
        }
        send_to_queue(message)

        return _response(202, {"mensagem": "Anúncio recebido e em processamento", "anuncio_id": body["anuncio_id"]})

    except Exception as e:
        return _response(500, {"erro": str(e)})


def _response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
