import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI


load_dotenv()

def get_azure_chat_llm() -> AzureChatOpenAI:
    api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
    deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")
    # endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    # api_key = os.environ.get("AZURE_OPENAI_API_KEY")

    llm = AzureChatOpenAI(
        azure_deployment=deployment_name,
        api_version=api_version,
        temperature=0.01,
        max_tokens=512,
        timeout=30,
        max_retries=2,
        # logprobs=True
    )

    return llm

