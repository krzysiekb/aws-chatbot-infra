#!/usr/bin/env python3

import aws_cdk as cdk

from base.github_trust_stack import GitHubTrustStack
from base.vpc_stack import VpcStack

app = cdk.App()

# Create the GitHub trust stack in AWS account.
GitHubTrustStack(app, "ChatbotGithubTrustStack")
VpcStack(app, "ChatbotVpcStack")

app.synth()
