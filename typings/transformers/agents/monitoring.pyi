"""
This type stub file was generated by pyright.
"""

from .agents import ReactAgent

def pull_message(step_log: dict): # -> Generator[Any, Any, None]:
    ...

def stream_to_gradio(agent: ReactAgent, task: str, **kwargs): # -> Generator[Any, Any, None]:
    """Runs an agent with the given task and streams the messages from the agent as gradio ChatMessages."""
    ...
