from aws_cdk import Stack, aws_lambda, aws_apigateway
from constructs import Construct


class BackendStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        backend_lambda = aws_lambda.Function(
            scope=self,
            id="ChatbotBackendLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="backend_lambda.handler",
            code=aws_lambda.Code.from_asset("backend/lambda"),
        )

        backend_apigw = aws_apigateway.LambdaRestApi(
            scope=self,
            id="ChatbotBackendAPI",
            handler=backend_lambda,
        )

        chatbot_res = backend_apigw.root.add_resource("chatbot")

        chatbot_res.add_method("GET")
        chatbot_res.add_method("POST")
