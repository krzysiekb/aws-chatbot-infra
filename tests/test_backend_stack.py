from aws_cdk import App, assertions

from backend.backend_stack import BackendStack


def test_backend_stack(app: App):
    backend_stack = BackendStack(app, "BackendStack", "../backend")

    template = assertions.Template.from_stack(backend_stack)

    template_json = template.to_json()

    template.has_resource_properties(
        "AWS::Lambda::Function", {
            "Handler": "backend_lambda.handler",
            "Layers": assertions.Match.any_value(),
            "Runtime": "python3.11"
        }
    )

    template.has_resource_properties(
        'AWS::Lambda::LayerVersion', {
            "CompatibleRuntimes": ["python3.11"],
        }
    )

    template.has_resource_properties(
        'AWS::ApiGateway::RestApi', {
            "Name": 'ChatbotBackendAPI'
        }
    )

    template.has_resource_properties(
        'AWS::ApiGateway::Resource', {
            'PathPart': 'chatbot'
        }
    )

    template.has_resource_properties(
        'AWS::ApiGateway::Method', {
            'HttpMethod': 'POST'
        }
    )
