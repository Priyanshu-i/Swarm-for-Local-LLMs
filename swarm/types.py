# swarm/types.py
from typing import List, Dict, Any, Optional, Callable  # Import Callable here

class Agent:
    def __init__(self, name: str, instructions: str, functions: List[Any] = None, model: str = "deepseek-r1:1.5b", tool_choice: str = None, parallel_tool_calls: bool = False):
        self.name = name
        self.instructions = instructions
        self.functions = functions or []
        self.model = model
        self.tool_choice = tool_choice
        self.parallel_tool_calls = parallel_tool_calls

class AgentFunction:
    def __init__(self, name: str, func: Callable):  # Now Callable is defined
        self.name = name
        self.func = func

class ChatCompletionMessage:
    def __init__(self, content: Optional[str], role: str, tool_calls: Optional[List[Any]] = None):
        self.content = content
        self.role = role
        self.tool_calls = tool_calls

class ChatCompletionMessageToolCall:
    def __init__(self, id: str, function: Any):
        self.id = id
        self.function = function

class Function:
    def __init__(self, name: str, arguments: str):
        self.name = name
        self.arguments = arguments

class Response:
    def __init__(self, messages: List[Dict[str, Any]], agent: Optional[Agent], context_variables: Dict[str, Any]):
        self.messages = messages
        self.agent = agent
        self.context_variables = context_variables

class Result:
    def __init__(self, value: str, agent: Optional[Agent] = None, context_variables: Dict[str, Any] = None):
        self.value = value
        self.agent = agent
        self.context_variables = context_variables or {}