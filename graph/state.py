from typing import List, TypedDict

class GraphState(TypedDict):
    """
    GraphState is a TypedDict that represents the state of a graph.
    Attributes:
        query (str): The query string.
        generation (str): The generation string.
        documents (List[str]): A list of document strings.
    """
    query: str
    generation: str
    documents: List[str]