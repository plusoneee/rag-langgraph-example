from typing import Any, Dict, List
from graph.state import GraphState
from ingestion import retriever
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"


class FakeRetriever:
    """
    A mock retriever class that simulates the retrieval of documents based on a query.
    """

    def invoke(self, query: str) -> List[str]:
        """
        Simulates the retrieval of documents by returning a fixed list of document identifiers.
        """
        return ["doc1", "doc2", "doc3"]


def retrieve(state: GraphState) -> Dict[str, Any]:
    """
    retrieve retrieves documents.
    Args:
        state (GraphState): The state of the graph.
    Returns:
        Dict[str, Any]: A dictionary containing the retrieved documents.
    """
    # Retrieve documents from the graph.
    print("retrieving documents")
    query = state["query"]
    documents = retriever.invoke(query)
    return {"documents": documents, "query": query}
