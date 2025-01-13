from typing import List
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from graph.llms import get_azure_chat_llm


def format_passages(passages: List[str]) -> str:
    formatted_passages = "\n".join(
        [f"[{i}] {passage}" for i, passage in enumerate(passages, 0)]
    )
    return formatted_passages


class DocumentRerank(BaseModel):
    ranking_index: List[int]


output_parser = PydanticOutputParser(pydantic_object=DocumentRerank)

rerank_index_prompt = """
You are RankGPT an intelligent assistant that can rank passages based on their relevancy to the query.
I will provide you with {passage_number} passages, each indicated by document list index number []. 
Rank the passages based on their relevance to query.

passages:
{passages}

query: {query}

now rank the passages based on their relevance to the query.
{format_instructions}
"""

rerank_prompt_template = PromptTemplate(
    input_variables=["passages", "query", "passage_number"],
    template=rerank_index_prompt,
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)

index_rerank_chain = rerank_prompt_template | get_azure_chat_llm() | output_parser
