from aws_cdk import Stack, aws_lambda
from constructs import Construct


class BackendStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        aws_lambda.Function(
            scope=self,
            id="ChatbotBackendLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="backend_lambda.handler",
            code=aws_lambda.Code.from_asset("backend/lambda"),
        )
