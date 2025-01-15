from graph.graph import app

if __name__ == "__main__":
    joy_config = {"configurable": {"thread_id": "joy"}}
    bob_config = {"configurable": {"thread_id": "bob"}}

    msg = "hello my name is joy"
    response = app.invoke({"history": [msg]}, joy_config)
    print("Joy:", msg, "\nAI: ", response["history"][-1].content)
    msg = "what is my name?"
    response = app.invoke({"history": [msg]}, joy_config)
    print("Joy:", msg, "\nAI: ", response["history"][-1].content)

    msg = "what is my name?"
    response = app.invoke({"history": [msg]}, bob_config)
    print("\nBob:", msg, "\nAI: ", response["history"][-1].content)
