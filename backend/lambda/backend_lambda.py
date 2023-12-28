import json

import boto3


def handler(event, context):
    body = event['body']
    print('request: {}'.format(json.dumps(body)))

    bedrock = boto3.client('bedrock-runtime')
    response = bedrock.invoke_model(
        modelId='amazon.titan-text-lite-v1',
        contentType='application/json',
        body=body
    )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': response['contentType']
        },
        'body': json.loads(response['body'])
    }
