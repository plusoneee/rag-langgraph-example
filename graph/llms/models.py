from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

def get_azure_llm(
    temperature: float = 0.01,
    max_token: int = 512,
    timeout: int = 30,
    max_retries: int = 2,
    api_version: str = "2024-08-01-preview",
    deployment_name: str = "gpt-4o-mini",
) -> AzureChatOpenAI:
    """
    Creates an instance of AzureChatOpenAI with the specified parameters.

    Args:
        temperature (float, optional): Sampling temperature to use. Defaults to 0.01.
        max_token (int, optional): Maximum number of tokens to generate. Defaults to 512.
        timeout (int, optional): Timeout duration for the request in seconds. Defaults to 30.
        max_retries (int, optional): Maximum number of retries for the request. Defaults to 2.
        api_version (str, optional): API version to use. Defaults to "2024-08-01-preview".
        deployment_name (str, optional): Name of the Azure deployment. Defaults to "gpt-4o-mini".
        AzureChatOpenAI: An instance of AzureChatOpenAI configured with the specified parameters.

    Returns:
        AzureChatOpenAI: An instance of AzureChatOpenAI configured with the specified parameters.
    """
    llm = AzureChatOpenAI(
        azure_deployment=deployment_name,
        api_version=api_version,
        temperature=temperature,
        max_tokens=max_token,
        timeout=timeout,
        max_retries=max_retries,
        # logprobs=True
    )

    return llm
