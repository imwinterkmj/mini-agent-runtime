# mini-agent-runtime

一个用于理解 Agent Runtime 底层机制的学习型小项目，不使用成熟的 Agent Framework。

## 当前范围

目前仅进行 Phase 0（项目初始化）。LLM Client、Agent Loop、Tool、Session、Context 管理和 Memory 均暂未实现。

## 环境要求

- Python 3.12

## 使用 Conda 配置环境（Windows PowerShell）

```powershell
conda create --name mini-agent-runtime python=3.12
conda activate mini-agent-runtime
python -m pip install -e ".[dev]"
```

## 运行检查

```powershell
python -m pytest
python main.py
```

## 学习路线

1. 项目初始化
2. 最小 LLM Client
3. Agent Loop
4. Tool Registry
5. Session 与 Context
6. Context 管理
7. 基础 Long-Term Memory
8. Tracing 与 Logging
9. 测试与文档
