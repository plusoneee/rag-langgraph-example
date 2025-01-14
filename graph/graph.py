from dotenv import load_dotenv
from langgraph.graph import END, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from graph.consts import GENERATE
from graph.nodes import generate
from graph.state import GraphState as RAGState

load_dotenv()

memory = MemorySaver()
workflow = StateGraph(RAGState)
workflow.add_node(GENERATE, generate)
workflow.set_entry_point(GENERATE)
workflow.add_edge(GENERATE, END)

# add memory checkpointer to the workflow
app = workflow.compile(checkpointer=memory)
