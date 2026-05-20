from rag.chunker import chunk_text
from rag.embedder import get_embeddings
from rag.vector_store import VectorStore

from tools.csv_tool import check_sensor_data
from tools.log_tool import check_logs
from tools.rule_tool import check_rules
from tools.rag_tool import create_rag_tool

from agent.agent import ResearchAgent


def load_data():
    with open("data/failure_logs.txt") as f:
        logs = f.read()

    with open("data/rules.txt") as f:
        rules = f.read()

    return logs + "\n" + rules


def main():

    print("🔄 Building RAG system...")

    # RAG setup
    text = load_data()
    chunks = chunk_text(text)

    embeddings = get_embeddings()
    store = VectorStore(embeddings)
    store.build(chunks)

    rag_tool = create_rag_tool(store)

    print("✅ RAG Ready\n")

    # Tools
    tools = [
        rag_tool,
        check_logs,
        check_sensor_data,
        check_rules
    ]

    agent = ResearchAgent(tools)

    # Query loop
    while True:
        query = input("\nAsk question (or 'exit'): ")

        if query.lower() == "exit":
            break

        result = agent.run(query)

        print("\n🧠 ANSWER:\n", result["answer"])
        print("\n💡 HYPOTHESES:\n", result["hypotheses"])
        print("\n✔ VERIFIED:\n", result["verified"])


if __name__ == "__main__":
    main()


    