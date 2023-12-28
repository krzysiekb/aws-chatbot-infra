#!/usr/bin/env python3

import aws_cdk as cdk

from backend.backend_stack import BackendStack
from base.github_trust_stack import GitHubTrustStack
from base.vpc_stack import VpcStack

app = cdk.App()

# Create the GitHub trust stack in AWS account.
GitHubTrustStack(app, "ChatbotGithubTrustStack")

VpcStack(app, "ChatbotVpcStack")
BackendStack(app, "ChatbotBackendStack")

app.synth()
