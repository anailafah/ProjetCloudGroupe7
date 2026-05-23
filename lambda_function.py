import json
from password_checker import analyze_password

def lambda_handler(event, context):

    body = json.loads(event.get("body", "{}"))
    password = body.get("password", "")

    if not password:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "password manquant"})
        }

    result = analyze_password(password)

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }