from aws_cdk import Stack
from constructs import Construct


class ModelStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        