
# AGENTS.md

## 项目定位

这是一个学习型的最小 Agent Runtime 项目。

目标不是做一个大而全的 Agent Framework，而是让我真正理解 AI Agent 应用开发中最核心的机制，为后续阅读和改造 DeepSeek Harness、Hermes Agent 做准备。

这个项目需要帮助我理解并能够解释：

- Agent Loop
- LLM 请求与响应流程
- Tool / Function Calling
- Tool Registry
- Session
- Context
- Long-Term Memory
- Context Compaction
- 基础 Tracing
- 基础测试

## 协作原则

当你协助这个仓库时，必须遵守以下规则：

1. 不要一次性生成整个项目。
2. 必须按阶段推进。
3. 在实现一个功能之前，先解释：
   - 它解决什么问题
   - 为什么需要它
   - 有哪些替代方案
4. 优先 Review 我已经写好的代码，而不是直接重写整个文件。
5. 如果出现 Bug：
   - 先定位根因
   - 解释为什么会发生
   - 再给出最小修改方案
6. 不要引入不必要的框架。
7. 不要过度工程化。
8. 保持代码模块化、可测试、容易理解。
9. 优先选择能暴露底层机制的简单实现。
10. 必须保留项目的学习价值，不要替我把关键部分全部自动生成。

## 技术约束

主要语言：

- Python 3.12

允许使用的基础依赖：

- httpx 或 requests
- python-dotenv
- pytest
- SQLite
- Python 标准库

除非 PROJECT_PLAN.md 明确进入对应阶段，否则不要引入：

- LangChain
- LlamaIndex
- Multi-Agent Framework
- RAG Framework
- 向量数据库
- Redis
- Kafka
- RabbitMQ
- Kubernetes
- Web 前端
- MCP

## 架构原则

项目应逐步拆分这些职责：

- LLM Client
- Agent Runtime
- Tool Registry
- Session Store
- Context Manager
- Memory Store
- Tracing

不要把所有逻辑都写进一个文件。

但也不要为了“看起来高级”提前建立大量抽象层。

原则是：

先有真实问题，再引入抽象。

## 学习目标

这个项目最终必须让我能够回答以下问题：

- 什么是 Agent Loop？
- Function Calling 到底是怎么工作的？
- LLM 是否真的执行了 Tool？
- 为什么需要 Tool Registry？
- Session、Context、Memory 有什么区别？
- 为什么不能把全部历史对话一直塞进 Prompt？
- Memory 什么时候应该写入？
- Memory 什么时候应该检索？
- 旧 Memory 和新 Memory 冲突时应该怎么办？
- 为什么 Agent Runtime 需要 Tracing？
- Tool 调用失败时 Agent 应该如何处理？
- 一个 Session 如何恢复？

## 阶段纪律

开始任何新任务之前，都要先读取：

- AGENTS.md
- PROJECT_PLAN.md
- PROGRESS.md

只允许做 PROGRESS.md 当前阶段对应的内容。

不要提前实现后续阶段的功能。

每完成一个阶段后必须：

1. 运行测试
2. 检查验收标准
3. 更新 PROGRESS.md
4. 给出建议的 Git Commit Message

## Code Review 要求

Review 代码时优先检查：

1. 正确性
2. 架构清晰度
3. 错误处理
4. 可测试性
5. 可读性
6. 简单性

不要提前做性能优化。

## 当前工作方式

如果因为上下文压缩、重新开启对话或切换线程导致之前内容丢失：

先重新读取：

- AGENTS.md
- PROJECT_PLAN.md
- PROGRESS.md

然后根据 PROGRESS.md 的 Current Phase 继续，不要重新规划整个项目。
