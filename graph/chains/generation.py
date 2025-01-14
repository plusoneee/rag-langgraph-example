from graph.llms.models import get_azure_llm
from langchain_core.output_parsers import StrOutputParser

chain = get_azure_llm() | StrOutputParser()