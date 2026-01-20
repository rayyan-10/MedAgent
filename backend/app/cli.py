from backend.app.agents.supervisor import graph
from backend.app.agents.prompts import SYSTEM_PROMPT
from backend.app.services.orchestration import parse_response


def run_cli():
    print("🧠 Mental Health AI Agent (CLI Mode)")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("User: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye 👋")
            break

        print(f"Received user input: {user_input[:200]}...")

        inputs = {
            "messages": [
                ("system", SYSTEM_PROMPT),
                ("user", user_input),
            ]
        }

        stream = graph.stream(inputs, stream_mode="updates")
        tool_called_name, final_response = parse_response(stream)

        print("\nTOOL CALLED:", tool_called_name)
        print("ANSWER:", final_response)
        print("-" * 60)


if __name__ == "__main__":
    run_cli()
