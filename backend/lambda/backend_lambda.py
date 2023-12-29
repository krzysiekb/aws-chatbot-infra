import json

import boto3

bedrock = boto3.client('bedrock-runtime')


def handler(event, context):
    request = json.loads(event['body'])
    print('request: {}'.format(json.dumps(request)))

    # Invoke the model
    input_message = request.get('inputMessage')
    body = json.dumps({
        'inputText': input_message,
        'textGenerationConfig': {
            'temperature': 0.0,
            'topP': 0.9,
            'maxTokenCount': 300,
        }
    })

    response = bedrock.invoke_model(
        modelId='amazon.titan-text-lite-v1',
        contentType='application/json',
        body=body
    )
    response_body = json.loads(response.get('body').read())

    print('response: {}'.format(json.dumps(response_body)))

    # Return the response
    output_message = response_body.get('results')[0].get('outputText')

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'inputMessage': input_message,
        'outputMessage': output_message
    }
