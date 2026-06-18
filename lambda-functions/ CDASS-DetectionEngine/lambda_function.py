import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CDASS-AttackerProfiles')

def lambda_handler(event, context):

    attacker_id = event.get('attacker_id', 'unknown')

    failed_logins = event.get('failed_logins', 0)
    unusual_requests = event.get('unusual_requests', 0)

    risk_score = min(
        (failed_logins * 0.1) +
        (unusual_requests * 0.15),
        1.0
    )

    deception_level = "LOW"

    if risk_score > 0.7:
        deception_level = "HIGH"
    elif risk_score > 0.4:
        deception_level = "MEDIUM"

    item = {
        "attacker_id": attacker_id,
        "timestamp": datetime.utcnow().isoformat(),
        "risk_score": str(risk_score),
        "deception_level": deception_level
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }
