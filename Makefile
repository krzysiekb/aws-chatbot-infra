cdk-bootstrap:
	cdk bootstrap

github-trust-stack:
    cdk deploy ChatbotGithubTrustStack \
        --parameters GitHubOrg=krzysiekb \
        --parameters GitHubRepo=aws-chatbot-infra

.PHONY: cdk-bootstrap github-trust-stack