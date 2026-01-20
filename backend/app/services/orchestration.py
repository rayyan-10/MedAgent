def parse_response(stream):
    tool_called = "None"
    final_response = None

    for s in stream:
        if "tools" in s:
            for msg in s["tools"].get("messages", []):
                tool_called = getattr(msg, "name", tool_called)

        if "agent" in s:
            for msg in s["agent"].get("messages", []):
                if msg.content:
                    final_response = msg.content

    return tool_called, final_response
