
# Mini Agent Runtime - Project Plan

## 1. 项目目标

从 0 实现一个最小 Agent Runtime，用来真正理解现代 AI Agent 系统背后的核心机制。

这个项目不是最终作品集项目，而是后续阅读和改造以下成熟项目的前置训练：

- DeepSeek Harness
- Hermes Agent

最终目标是为后续正式项目做准备：

Long-Term Memory / Agent Runtime Extension。

本仓库必须保持小而清晰，不允许无限扩张。

## 2. 最终需要具备的能力

项目结束时应支持：

- 基础 LLM 通信
- Agent Loop
- Tool Calling
- Tool Registry
- 多轮 Session
- Session 持久化
- 基础 Context 管理
- 简单 Long-Term Memory
- Memory 检索与 Prompt 注入
- 基础 Tracing / Logging
- 自动化测试

## 3. 明确不做的内容

这个项目不做：

- 完整 RAG 系统
- 向量数据库
- Multi-Agent
- MCP
- 复杂 Planner
- Web UI
- 分布式架构
- LangChain
- LlamaIndex
- Redis
- MQ
- Kubernetes

这些全部留到后续正式项目。

---

# Phase 0：项目初始化

## 目标

建立干净、规范、可测试的 Python 项目。

## 需要完成

- Python 3.12
- 虚拟环境
- 依赖管理
- `.env.example`
- `.gitignore`
- README
- pytest
- 基础 logging
- 合理 package 结构

建议结构：

mini-agent-runtime/
├── src/
│   └── mini_agent/
├── tests/
├── .env.example
├── .gitignore
├── README.md
├── AGENTS.md
├── PROJECT_PLAN.md
├── PROGRESS.md
└── pyproject.toml

## 验收标准

- 项目能够正常运行
- pytest 能正常执行
- API Key 不进入 Git
- 基础目录结构明确

---

# Phase 1：最小 LLM Client

## 目标

理解模型调用的基础生命周期。

## 学习内容

- system / user / assistant message
- HTTP Request
- Model Response
- temperature
- max tokens
- timeout
- API error handling

## 实现内容

实现一个最简单的 LLM Client。

流程：

User Input
↓
LLM Client
↓
Model
↓
Text Response

## 验收标准

可以在终端输入一句话并获得模型回答。

---

# Phase 2：Agent Loop

## 目标

实现 Agent Runtime 最核心的循环。

流程：

User
↓
LLM
↓
判断
├── 普通回答 → 返回用户
└── Tool Call
      ↓
   执行 Tool
      ↓
   Tool Result
      ↓
      LLM
      ↓
   最终回答

## 必须理解

- 为什么需要 Agent Loop
- LLM 不是真的执行 Tool
- Tool Call 本质上是什么
- 为什么 Tool Result 还要再次送回 LLM
- Agent Loop 应该在什么情况下结束

## 验收标准

模型可以自主判断：

- 直接回答
- 或调用一个 Tool

并且 Tool 执行结果能够返回给模型继续生成最终回答。

---

# Phase 3：Tool Registry

## 目标

把 Tool 从 Agent Loop 中解耦。

建议结构：

tools/
├── calculator.py
├── time_tool.py
└── registry.py

每个 Tool 需要包含：

- name
- description
- parameters schema
- callable function

## 必须理解

- 为什么不能把 Tool 写死在 Agent Loop 里
- Tool Registry 提供了什么抽象
- 如何增加一个新 Tool 而不修改 Agent Loop

## 验收标准

新增一个 Tool 时：

不需要修改 Agent Loop 核心逻辑。

---

# Phase 4：Session

## 目标

支持多轮对话和 Session 恢复。

## 实现内容

- session_id
- message history
- system / user / assistant / tool 消息
- 不同 session 隔离
- SQLite 持久化
- Session 恢复

## 必须理解

Session、Context、Memory 三者的区别。

## 验收标准

程序退出后再次启动：

可以通过 session_id 恢复之前对话。

---

# Phase 5：Context 管理

## 目标

解决长对话不断增长的问题。

## 第一版策略

可以实现：

- 最近 N 条消息
- 最大 message 数
- 简单 summary

不要做复杂 Compaction。

## 必须理解

- 为什么不能无限传全部历史
- Context Window 是什么
- Token Cost 为什么会上升
- 为什么需要裁剪或压缩 Context

## 验收标准

长 Session 不会无限增长 Prompt。

---

# Phase 6：基础 Long-Term Memory

## 目标

让信息可以跨 Session 保留。

建议数据结构：

memory

- id
- user_id
- type
- content
- created_at
- updated_at

流程：

Memory Write
↓
SQLite
↓
Memory Retrieval
↓
Prompt Injection

## 第一版检索方式

使用：

- keyword search
- SQLite FTS

暂时不要上向量数据库。

## 必须理解

- 什么信息应该成为 Memory
- 什么信息只属于 Session Context
- Memory 什么时候写入
- Memory 什么时候读取
- Memory 如何注入 Prompt
- Memory 如何删除
- Memory 如何更新
- Memory 冲突怎么处理

示例：

旧 Memory：

用户主要使用 Java。

新信息：

用户现在主要使用 Go。

系统不能简单同时永久保留两条互相冲突的信息。

需要考虑：

- UPDATE
- REPLACE
- VERSION
- TIMESTAMP

## 验收标准

新 Session 中能够检索并使用旧 Session 保存的重要信息。

---

# Phase 7：Tracing / Logging

## 目标

理解 Agent 可观测性。

## 至少记录

- session_id
- model call
- model latency
- tool call
- tool latency
- memory retrieval
- errors

## 必须理解

为什么生产 Agent 系统必须有 Trace。

## 验收标准

一次 Agent 执行过程可以通过日志基本还原。

---

# Phase 8：测试与收尾

## 至少编写

- Tool Registry Test
- Session Test
- Memory Test
- Agent Loop Test

如果真实 LLM 不适合测试，可以使用 Mock。

## README 最终需要说明

1. 项目目标
2. 架构
3. Agent Loop
4. Tool Registry
5. Session / Context / Memory 区别
6. 如何运行
7. 已知限制
8. 下一步计划

## 项目停止条件

完成 Phase 8 后停止扩展本仓库。

下一阶段：

阅读 DeepSeek Harness 和 Hermes Agent，并进入正式作品集项目：

Long-Term Memory / Agent Runtime Extension。
