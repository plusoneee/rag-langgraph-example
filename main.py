from graph.graph import app

if __name__ == "__main__":
    questions = "What did the president say about Justice Breyer"
    answer = app.invoke({"query": questions})

    print('Question:', answer.get("query"))
    print('Answer:', answer.get("generation"))
