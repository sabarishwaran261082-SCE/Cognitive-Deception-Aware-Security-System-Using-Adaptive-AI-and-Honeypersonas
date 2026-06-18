import json
import boto3
from datetime import datetime

sqs = boto3.client('sqs')

QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/208519603970/CDASS-SecurityAlerts"

def lambda_handler(event, context):

    alert = {
        "attacker_id": event.get("attacker_id", "unknown"),
        "attack_type": event.get("attack_type", "UNKNOWN_ATTACK"),
        "persona": event.get("persona", "Unknown Persona"),
        "severity": event.get("severity", "HIGH"),
        "timestamp": datetime.utcnow().isoformat()
    }

    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(alert)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Alert sent to SQS",
            "alert": alert,
            "message_id": response["MessageId"]
        })
    }
