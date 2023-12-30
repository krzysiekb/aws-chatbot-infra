# AWS Chatbot

Repository contains simple chatbot, built using AWS Lambda and Amazon Bedrock.

Project is deployed in AWS using combination of CDK and GitHub Actions. GitHub Actions are 
authenticated with AWS account using OIDC. Trust relationship is established and Github Actions
are allowed to assume roles created by CDK bootstrap in AWS Account. This enables CDK running 
in GitHub Actions to deploy AWS resources.

## Deploy

### Setup AWS account

1. Create AWS account
2. Bootstrap CDK (https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)
```
make cdk-bootstrap
```
3. Setup OIDC for GitHub Actions  
    3.1 Modify makefile to include your GitHub organization and repository name 
    ```
    GITHUB_ORG=krzysiekb
    GIHUB_REPO=aws-chatbot-infra
    ```
    3.2 Then execute target to set up OIDC for GitHub Actions
    ```
    make github-trust-stack
    ```
4. Run cdk-deploy GitHub Action to deploy Chatbot infrastructure.