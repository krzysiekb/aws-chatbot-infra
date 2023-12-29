from aws_cdk import Stack, assertions
from aws_cdk.assertions import Match

from base.vpc_stack import VpcStack


def test_vpc_stack(app):
    vpc_stack = VpcStack(app, "TestVpcStack")

    template = assertions.Template.from_stack(vpc_stack)

    template.has_resource_properties("AWS::EC2::VPC", {
        "CidrBlock": "10.0.0.0/16",
        "EnableDnsHostnames": True,
        "EnableDnsSupport": True,
    })

    template.has_resource_properties("AWS::EC2::Subnet", {
        "VpcId": Match.any_value(),
        "CidrBlock": "10.0.0.0/24",
        "MapPublicIpOnLaunch": True,
    })

    template.has_resource_properties("AWS::EC2::Subnet", {
        "VpcId": Match.any_value(),
        "CidrBlock": "10.0.1.0/24",
        "MapPublicIpOnLaunch": True,
    })

    template.has_resource_properties("AWS::EC2::Subnet", {
        "VpcId": Match.any_value(),
        "CidrBlock": "10.0.2.0/24",
        "MapPublicIpOnLaunch": False,
    })

    template.has_resource_properties("AWS::EC2::Subnet", {
        "VpcId": Match.any_value(),
        "CidrBlock": "10.0.3.0/24",
        "MapPublicIpOnLaunch": False,
    })
