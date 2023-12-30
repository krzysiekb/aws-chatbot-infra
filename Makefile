GITHUB_ORG=krzysiekb
GIHUB_REPO=aws-chatbot-infra

cdk-bootstrap:
	cdk bootstrap

github-trust-stack:
    cdk deploy ChatbotGithubTrustStack \
        --parameters GitHubOrg=${GITHUB_ORG} \
        --parameters GitHubRepo=${GIHUB_REPO}

.PHONY: cdk-bootstrap github-trust-stack