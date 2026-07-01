import ollama


def chat(model: str, messages: list):

    response = ollama.chat(
        model=model,
        messages=messages
    )

    return response