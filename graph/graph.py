from dotenv import load_dotenv
from langgraph.graph import END, StateGraph
from graph.consts import RERANK_DOCUMENTS, GENERATE, RETRIEVE
from graph.nodes import retrieve, generate, rerank_documents
from graph.state import GraphState as RAGState

load_dotenv()

workflow = StateGraph(RAGState)
workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(RERANK_DOCUMENTS, rerank_documents)
workflow.add_node(GENERATE, generate)
workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, RERANK_DOCUMENTS)

# workflow.add_edge(RERANK_DOCUMENTS, END)
workflow.add_edge(RERANK_DOCUMENTS, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()
# app.get_graph().draw_mermid_png('output.png')