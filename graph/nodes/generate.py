from typing import Any, Dict
from langchain_core.messages import AIMessage
from graph.chains.generation import chain
from graph.state import GraphState

def generate(state: GraphState) -> Dict[str, Any]:
    response = chain.invoke(state["history"])
    return {
        "history": [AIMessage(response)],
    }
