from typing import Any, Dict
from graph.state import GraphState
from graph.chains.retrieval_rerank import (
    index_rerank_chain,
    format_passages,
    DocumentRerank,
)


def rerank_documents(state: GraphState) -> Dict[str, Any]:
    query = state["query"]
    documents = state["documents"]
    formatted_passages = format_passages(documents)

    output: DocumentRerank = index_rerank_chain.invoke(
        {
            "passages": formatted_passages,
            "query": query,
            "passage_number": len(documents),
        }
    )

    ranking_index = output.ranking_index

    try:
        reranked_docs = [documents[i] for i in ranking_index]
    except IndexError:
        raise ValueError(
            f"Invalid rerank order: {ranking_index}. Ensure indices are within range."
        )

    return {"documents": reranked_docs, "query": query}
