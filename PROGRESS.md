
# PROGRESS.md

## Current Phase

Phase 1：最小 LLM Client

## Status

待开始

## Completed

### Phase 0：项目初始化

- 已确定项目定位与长期路线
- 已使用 Conda 创建 Python 3.12 环境
- 已建立 `src` package 结构
- 已配置 `pyproject.toml` 与 pytest
- 已配置 `.env.example` 和 `.gitignore`
- 已建立基础 README
- 已实现标准库基础 logging
- 已添加 package smoke test 和 logging 配置测试
- Phase 0 验收通过：程序可运行，pytest 共 2 项测试通过

## Current Tasks

- 尚未开始 Phase 1 实现
- 明确最小 LLM Client 的请求与响应边界
- 选择 `httpx` 或 `requests`
- 读取环境变量中的 API 配置
- 实现一次终端文本问答

## Acceptance Criteria

Phase 1 完成前必须满足：

- 可以在终端输入一句话并获得模型回答
- 能构造 system / user / assistant 消息
- 支持 timeout 和基础 API 错误处理
- API Key 不进入 Git

## Next

Phase 2：Agent Loop

在 Phase 1 完成之前不要提前进入 Phase 2。

## Important Decisions

- 使用 Python 3.12
- 使用 Conda 管理项目环境
- 不使用 LangChain
- 不使用 LlamaIndex
- 不使用成熟 Agent Framework
- 本项目只做最小 Agent Runtime
- 正式作品集将在后续基于 DeepSeek Harness / Hermes Agent 展开

## Known Issues

- 暂无
