from typing import Any, Dict
from graph.state import GraphState
from graph.chains.generation import generation_chain


def generate(state: GraphState) -> Dict[str, Any]:
    query = state["query"]
    documents = state["documents"]
    generation = generation_chain.invoke(
        {
            "context": documents,
            "question": query,
        }
    )
    return {"generation": generation, "query": query, "documents": documents}
