import aws_cdk as cdk

from aws_cdk import aws_ec2


class VpcStack(cdk.Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        vpc = cdk.aws_ec2.Vpc(
            self,
            "ChatbotVpc",
            cidr="10.0.0.0/16",
            max_azs=3,
            subnet_configuration=[
                cdk.aws_ec2.SubnetConfiguration(
                    name="ChatbotPublicSubnet",
                    subnet_type=aws_ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                cdk.aws_ec2.SubnetConfiguration(
                    name="ChatbotPrivateSubnet",
                    subnet_type=aws_ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ],
            nat_gateways=1,
            nat_gateway_provider=aws_ec2.NatProvider.gateway(),
            create_internet_gateway=True,
        )


