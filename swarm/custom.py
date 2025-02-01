from typing import List, Dict, Any, Optional

class Function:
    def __init__(self, name: str, arguments: str):
        self.name = name
        self.arguments = arguments

class ChatCompletionMessageToolCall:
    def __init__(self, id: str, function: Function):
        self.id = id
        self.function = function

class ChatCompletionMessage:
    def __init__(self, content: Optional[str], role: str, tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None):
        self.content = content
        self.role = role
        self.tool_calls = tool_calls

def chat_with_local_model(messages: List[Dict[str, str]], model: str = "deepseek-r1:1.5b") -> ChatCompletionMessage:
    import ollama

    prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    response = ollama.generate(model=model, prompt=prompt)
    generated_content = response['response']
    return ChatCompletionMessage(content=generated_content, role="assistant")