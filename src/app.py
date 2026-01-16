import json
import boto3
import os
import uuid
from datetime import datetime

# Initialize clients outside the handler for connection reuse (Latency optimization)
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
table = dynamodb.Table(os.environ['TABLE_NAME'])
bucket_name = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    try:
        # 1. Parse Input
        body = json.loads(event['body'])
        transaction_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()

        # 2. S3 Audit Logging (Traceability)
        s3.put_object(
            Bucket=bucket_name,
            Key=f"logs/{transaction_id}.json",
            Body=json.dumps(body)
        )

        # 3. Process & Save to DynamoDB
        item = {
            'TransactionId': transaction_id,
            'Timestamp': timestamp,
            'Amount': body.get('amount'),
            'Status': 'COMPLETED',
            'UserId': body.get('user_id')
        }
        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Success", "id": transaction_id})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal Server Error"})
        }