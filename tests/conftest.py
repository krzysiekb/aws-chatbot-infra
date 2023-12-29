import pytest
from aws_cdk import App


@pytest.fixture
def app() -> App:
    return App()