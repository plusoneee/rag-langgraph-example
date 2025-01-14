from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class GraphState(TypedDict):
    """
    GraphState is a TypedDict that represents the state of a graph.
    Attributes:
        history (Sequence[BaseMessage]): A sequence of messages.
    """

    history: Annotated[Sequence[BaseMessage], add_messages]
