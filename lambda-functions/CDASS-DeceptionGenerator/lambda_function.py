import json
import boto3
from datetime import datetime
import os

s3 = boto3.client("s3")

BUCKET = os.environ["BUCKET_NAME"]

def lambda_handler(event, context):

    attacker_id = event.get("attacker_id", "unknown")
    risk_score = event.get("risk_score", "HIGH")

    persona = {
        "attacker_id": attacker_id,
        "risk_level": risk_score,
        "persona": "Senior Cloud Administrator",
        "environment": "Financial Transaction Database",
        "deception_strategy": "Credential Harvest Trap",
        "generated_at": datetime.utcnow().isoformat()
    }

    key = f"deception-templates/{attacker_id}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(persona),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": json.dumps(persona)
    }
