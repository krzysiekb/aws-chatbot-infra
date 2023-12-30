# AWS Chatbot

Repository contains simple chatbot, built using AWS Lambda and Amazon Bedrock.

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