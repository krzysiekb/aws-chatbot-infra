#!/usr/bin/env python3
import os

import aws_cdk as cdk

from base.vpc_stack import VpcStack


app = cdk.App()

VpcStack(scope=app, id="ChatbotVpcStack")

app.synth()
