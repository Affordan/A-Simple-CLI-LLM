# Chat CLI - 智能聊天客户端

一个模块化的智能聊天CLI工具，支持前后端分离架构。

## 🏗️ 项目结构

```
chat-cli/                     # 项目根目录
├── __init__.py              # 包初始化文件
├── main.py                  # 主入口文件（CLI命令定义）
├── pyproject.toml           # 项目配置文件
├── README.md                # 项目说明文档
├── backend/                 # 后端模块
│   ├── __init__.py
│   └── server.py            # FastAPI服务器
├── frontend/                # 前端模块
│   ├── __init__.py
│   └── chat.py              # 交互式聊天逻辑
└── utils/                   # 工具模块
    ├── __init__.py
    ├── api_client.py        # API请求处理
    └── ui.py                # 界面显示功能
```

## 🚀 安装和使用

### 安装依赖

```bash
cd chat-cli
pip install -e .
```

### 使用方法

#### 1. 显示帮助信息
```bash
python main.py
# 或者
python main.py help
```

#### 2. 启动交互式聊天
```bash
python main.py start
```

#### 3. 使用指定模型开始聊天
```bash
python main.py start --model gpt-4
```

#### 4. 仅启动后端服务器
```bash
python main.py server
```

#### 5. 一次性问答
```bash
python main.py chat "你好，请介绍一下自己"
```

### 环境配置

确保设置了环境变量：
```bash
export DEEPSEEK_API_KEY="your_api_key_here"
```

## 📦 模块说明

### Backend模块 (`backend/`)
- **server.py**: FastAPI后端服务
  - `/chat` - 聊天API端点
  - `/health` - 健康检查端点
  - 支持流式响应
  - 自动错误处理

### Frontend模块 (`frontend/`)
- **chat.py**: 前端交互逻辑
  - `interactive_chat()` - 完整聊天会话
  - `chat_with_prompt()` - 单次问答
  - `start_server_process()` - 服务器进程管理

### Utils模块 (`utils/`)
- **api_client.py**: API通信
  - `send_chat_request()` - 发送聊天请求
  - `check_server_health()` - 服务器状态检查
- **ui.py**: 用户界面
  - 帮助信息显示
  - 彩色消息输出
  - 界面布局管理

## 🎨 交互式命令

在聊天会话中可以使用以下命令：

- `/help` - 显示帮助
- `/clear` - 清空聊天历史
- `/model` - 切换AI模型
- `/exit` 或 `/quit` - 退出聊天

## 🔧 开发

### 项目架构优势
1. **模块化设计**: 前后端完全分离
2. **可维护性**: 职责清晰，易于扩展
3. **可重用性**: 各模块可独立使用
4. **标准结构**: 符合Python包规范

### 扩展指南
- 添加新的AI模型支持：修改 `backend/server.py`
- 增加新的CLI命令：修改 `main.py`
- 改进用户界面：修改 `utils/ui.py`
- 添加新的API客户端：扩展 `utils/api_client.py`

## 📝 示例

```bash
# 快速开始聊天
python -m chat-cli.main start

# 使用不同模型
python -m chat-cli.main start --model deepseek-chat

# 单次提问
python -m chat-cli.main chat "解释什么是机器学习"

# 后台运行服务器
python -m chat-cli.main server --host 0.0.0.0 --port 8080
```

## ⚠️ 注意事项

1. 首次使用前请确保设置了 `DEEPSEEK_API_KEY` 环境变量
2. 默认服务器运行在 `127.0.0.1:8000`
3. 使用 Ctrl+C 可以随时退出程序
4. 聊天历史在会话期间会保持，使用 `/clear` 可以清空
