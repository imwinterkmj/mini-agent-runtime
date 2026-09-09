# mini-agent-runtime

A small learning project for understanding the mechanics behind an agent runtime without using a mature agent framework.

## Current scope

Only Phase 0 (project initialization) is in progress. LLM clients, agent loops, tools, sessions, context management, and memory are intentionally not implemented yet.

## Requirements

- Python 3.12

## Setup with Conda (Windows PowerShell)

```powershell
conda create --name mini-agent-runtime python=3.12
conda activate mini-agent-runtime
python -m pip install -e ".[dev]"
```

## Checks

```powershell
python -m pytest
python main.py
```

## Learning roadmap

1. Project initialization
2. Minimal LLM client
3. Agent loop
4. Tool registry
5. Session and context
6. Context management
7. Basic long-term memory
8. Tracing and logging
9. Tests and documentation
