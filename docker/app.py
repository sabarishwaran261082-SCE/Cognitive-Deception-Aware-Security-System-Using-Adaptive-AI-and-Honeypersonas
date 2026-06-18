import json
import joblib
import pandas as pd

# Load models during container startup
classifier = joblib.load(
    "models/cdass_attack_classifier.pkl"
)

encoder = joblib.load(
    "models/cdass_label_encoder.pkl"
)

anomaly_detector = joblib.load(
    "models/cdass_anomaly_detector.pkl"
)

def lambda_handler(event, context):

    body = event

    failed_logins = body.get("failed_logins", 0)
    port_scans = body.get("port_scans", 0)
    iam_changes = body.get("iam_changes", 0)
    s3_access = body.get("s3_access", 0)

    sample = pd.DataFrame(
        [[
            failed_logins,
            port_scans,
            iam_changes,
            s3_access
        ]],
        columns=[
            "failed_logins",
            "port_scans",
            "iam_changes",
            "s3_access"
        ]
    )

    anomaly = anomaly_detector.predict(sample)

    if anomaly[0] == -1:

        return {
            "statusCode": 200,
            "body": json.dumps({
                "attack_type":
                "UNKNOWN_ATTACK",

                "response":
                "Deploy High Interaction Honeynet"
            })
        }

    prediction = classifier.predict(sample)

    attack_type = encoder.inverse_transform(
        prediction
    )[0]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "attack_type":
            attack_type,

            "response":
            "Deploy Adaptive Persona"
        })
    }
