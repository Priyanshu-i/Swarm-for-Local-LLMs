# Swarm for Local LLMs 🐝

This project demonstrates how to use a **Swarm framework** to manage and interact with **local Large Language Models (LLMs)** using [Ollama](https://github.com/ollama/ollama). The Swarm framework allows you to create multiple agents, each with its own instructions and capabilities, and seamlessly transfer control between them during a conversation.

## Project Overview

The **Swarm for Local LLMs** project is designed to simulate a multi-agent system where each agent can handle specific tasks or domains. For example:
- **Agent A**: A general-purpose assistant that can transfer conversations to specialized agents.
- **Agent B**: A specialized agent that explains concepts in 1700s English.

This project is particularly useful for:
- **Local LLM experimentation**: Run and test LLMs locally without relying on cloud-based APIs.
- **Multi-agent systems**: Create and manage multiple agents with distinct roles and capabilities.
- **Agent handoff**: Seamlessly transfer conversations between agents based on user requests.

## Features

- **Local LLM Integration**: Uses [Ollama](https://github.com/ollama/ollama) to run local LLMs like `deepseek-r1:1.5b`.
- **Swarm Framework**: Manages multiple agents and their interactions.
- **Agent Handoff**: Transfers conversations between agents dynamically.
- **Customizable Agents**: Each agent can have its own instructions, functions, and behavior.
- **REPL Interface**: Provides a simple command-line interface for interacting with the Swarm.

## Repository Link

🔗 [GitHub Repository](https://github.com/Priyanshu-i/Swarm-for-Local-LLMs)

---

## Getting Started

### Prerequisites

1. **Python 3.7+**: Ensure you have Python installed on your system.
2. **Ollama**: Install Ollama to run local LLMs. Follow the [Ollama installation guide](https://github.com/ollama/ollama) to set it up.
3. **Local LLM**: Download a local LLM like `deepseek-r1:1.5b` using Ollama:
   ```bash
   ollama pull deepseek-r1:1.5b
   ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Priyanshu-i/Swarm-for-Local-LLMs.git
   cd Swarm-for-Local-LLMs
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Swarm

1. Start the Swarm by running the `agent_handoff.py` script:
   ```bash
   python agent_handoff.py
   ```

2. Interact with the agents:
   - The conversation starts with **Agent A**.
   - Request to talk to **Agent B** by saying: `I want to talk to agent B, have him explain LLMs.`
   - **Agent B** will respond in 1700s English.

### Example Output

```
Swarm client initialized
Agent A created
Agent B created
Starting conversation with Agent A
Transferring to Agent B
Final response:
Agent B: Verily, I shall elucidate upon the matter of Large Language Models, which art the marvels of modern computation...
```

---

## Code Structure

The repository is organized as follows:

```
Swarm-for-Local-LLMs/
├── agent_handoff.py          # Example script to demonstrate agent handoff
├── swarm/                    # Swarm framework implementation
│   ├── __init__.py           # Package initialization
│   ├── core.py               # Core Swarm and Agent classes
│   ├── repl.py               # REPL interface for interacting with the Swarm
│   ├── util.py               # Utility functions
│   ├── types.py              # Custom types and classes
│   └── custom.py             # Custom classes for mimicking OpenAI's API
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## Customizing Agents

You can create and customize your own agents by modifying the `agent_handoff.py` script. For example:

```python
agent_c = Agent(
    name="Agent C",
    instructions="You are a math expert. Explain mathematical concepts in simple terms.",
    functions=[],  # Add custom functions if needed
)
```

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Ollama](https://github.com/ollama/ollama) for providing the local LLM infrastructure.
- Inspired by the concept of **Swarm Intelligence** and multi-agent systems.

---

## Contact

For questions or feedback, feel free to reach out:

- **Priyanshu Singh**  
  GitHub: [Priyanshu-i](https://github.com/Priyanshu-i)  

---

Enjoy experimenting with the Swarm for Local LLMs! 🚀
