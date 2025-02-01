from swarm import Swarm, Agent
from swarm.types import Result, FunctionDef

client = Swarm()
print("Swarm client initialized")

# --- Define Agent B FIRST to avoid reference issues ---
agent_b = Agent(
    name="Agent B",
    instructions="I explain everything in 1700s English. Your job is to explain Large Language Models (LLMs) in a historical style.",
)
print("Agent B created")

# --- Transfer function with proper metadata ---
def transfer_to_agent_b():
    """Transfers the conversation to Agent B when requested"""
    print("Transferring to Agent B")
    return Result(value="Transferring to Agent B", agent=agent_b)

transfer_function = FunctionDef(
    name="transfer_to_agent_b",
    description="Call this IMMEDIATELY when the user asks to speak with Agent B",
    function=transfer_to_agent_b
)

# --- Create Agent A with the transfer function ---
agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent. Your ONLY JOB is to transfer users to Agent B when requested. Call transfer_to_agent_b IMMEDIATELY if the user asks for Agent B.",
    functions=[transfer_function],
)
print("Agent A created")

# --- Modified client run logic ---
print("Starting conversation with Agent A")
messages = [{"role": "user", "content": "I want to talk to agent B, have him explain LLMs."}]

# Get initial response
response = client.run(
    agent=agent_a,
    messages=messages,
    max_steps=3  # Prevent infinite loops
)

print("\nFinal response:")
print(response.messages[-1]["content"])