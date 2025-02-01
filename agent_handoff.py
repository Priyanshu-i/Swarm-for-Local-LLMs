from swarm import Swarm, Agent
from swarm.types import Result  # Import Result class

client = Swarm()
print("Swarm client initialized")

def transfer_to_agent_b():
    """Transfer agent A users immediately to Agent B."""
    print("Transferring to Agent B")
    return Result(value="Transferring to Agent B", agent=agent_b)  # Return a Result object with agent_b

agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent. If the user wants to talk to Agent B, call the transfer_to_agent_b function immediately.",
    functions=[transfer_to_agent_b],
)
print("Agent A created")

agent_b = Agent(
    name="Agent B",
    instructions="I explain everything in 1700s English. Your job is to explain Large Language Models (LLMs) in a historical style.",
)
print("Agent B created")

print("Starting conversation with Agent A")
messages = [{"role": "user", "content": "I want to talk to agent B, have him explain LLMs."}]
response = client.run(agent_a, messages=messages)

print("Final response:")
print(response.messages[-1]["content"])