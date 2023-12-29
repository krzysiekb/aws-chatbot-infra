from aws_cdk import Stack, CfnParameter, CfnOutput
from aws_cdk.aws_iam import (
    CfnOIDCProvider,
    Role,
    FederatedPrincipal,
    PolicyStatement,
    Effect,
)
from constructs import Construct


class GitHubTrustStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # parameters
        github_org = CfnParameter(scope=self, id="GitHubOrg", type="String")
        github_repo = CfnParameter(scope=self, id="GitHubRepo", type="String")

        # GitHub OIDC provider
        # https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#creating-an-oidc-provider
        #
        # Thumbprints are from:
        # https://github.blog/changelog/2022-01-13-github-actions-update-on-oidc-based-deployments-to-aws/

        github_provider = CfnOIDCProvider(
            scope=self,
            id="GitHubOIDCProvider",
            thumbprint_list=["6938fd4d98bab03faadb97b34396831e3780aea1"],
            url="https://token.actions.githubusercontent.com",
            client_id_list=["sts.amazonaws.com"],
        )

        github_actions_role = Role(
            scope=self,
            id="GitHubActionsRole",
            assumed_by=FederatedPrincipal(
                federated=github_provider.attr_arn,
                conditions={
                    "StringEquals": {
                        # audience is sts.amazonaws.com (must be set to sts.amazonaws.com)
                        "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
                    },
                    "StringLike": {
                        # subscriber is main branch of the defined repository
                        "token.actions.githubusercontent.com:sub": f"repo:{github_org.value_as_string}/{github_repo.value_as_string}:ref:refs/heads/main"
                    },
                },
                assume_role_action="sts:AssumeRoleWithWebIdentity",
            ),
        )

        # this policy allows GitHub Actions to assume the roles for:
        # file publishing, lookup and deploy created by CDK bootstrap
        # https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html
        accume_cdk_deployments_role_policy = PolicyStatement(
            effect=Effect.ALLOW,
            actions=["sts:AssumeRole"],
            resources=["arn:aws:iam::*:role/cdk-*"],
            conditions={
                "StringEquals": {
                    "aws:ResourceTag/aws-cdk:bootstrap-role": [
                        "file-publishing",
                        "lookup",
                        "deploy",
                    ]
                }
            },
        )

        github_actions_role.add_to_policy(accume_cdk_deployments_role_policy)

        # outputs
        CfnOutput(
            scope=self,
            id="GitHubActionsRoleArn",
            value=github_actions_role.role_arn,
            description="GitHub Actions role ARN",
        )
