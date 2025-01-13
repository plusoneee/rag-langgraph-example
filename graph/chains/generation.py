from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from graph.llms.models import get_azure_llm

prompt = hub.pull("rlm/rag-prompt")
generation_chain = prompt | get_azure_llm() | StrOutputParser()