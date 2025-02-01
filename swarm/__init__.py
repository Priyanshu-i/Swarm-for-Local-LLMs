# swarm/__init__.py
from .core import Swarm, Agent
from .repl import run_demo_loop

__all__ = ["Swarm", "Agent", "run_demo_loop"]