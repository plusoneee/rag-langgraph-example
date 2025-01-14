from uuid import uuid4
from graph.graph import app
from langchain_core.messages import AIMessage

if __name__ == "__main__":
    thread_uuid = str(uuid4())

    config = {"configurable": {"thread_id": thread_uuid}}
    print("Hello, What can I do for you? (type 'q' or 'exit' to quit)")
    
    while True:
        _input = input("You: ")

        if _input == "q" or _input == "exit":
            print("AI: goodbye!")
            break

        for event in app.stream({"history": _input}, config, stream_mode="values"):
            if event.get("history") and isinstance(event["history"][-1], AIMessage):
                print("AI:", event["history"][-1].content)
