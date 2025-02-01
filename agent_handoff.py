# agent_handoff.py
from swarm import Swarm, Agent

client = Swarm()
print("Swarm client initialized")

def transfer_to_agent_b():
    """Transfer agent a users immediately."""
    print("Transferring to Agent B")
    return agent_b

agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)
print("Agent A created")

agent_b = Agent(
    name="Agent B",
    instructions="I explain everything in 1700s english.",
)
print("Agent B created")

print("Starting conversation with Agent A")
messages = [{"role": "user", "content": "I want to talk to agent B, have him explain LLMs."}]
response = client.run(agent_a, messages=messages)

print("Final response : ")
print(response.messages[-1]["content"])