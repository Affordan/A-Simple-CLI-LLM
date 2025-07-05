"""
FastAPI后端服务器
提供聊天API接口
"""
import os
import json
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from openai import OpenAI
from sse_starlette.sse import EventSourceResponse
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# FastAPI应用实例
app = FastAPI(title="Chat CLI Backend", description="智能聊天后端API")


# Pydantic数据模型
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = 'deepseek-chat'
    stream: bool = True


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """聊天API端点"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = "https://api.deepseek.com/v1"

    if not api_key:
        raise HTTPException(status_code=400, detail="DEEPSEEK_API_KEY 环境变量未设置")

    client = OpenAI(api_key=api_key, base_url=base_url)

    try:
        response = client.chat.completions.create(
            model=request.model,
            messages=[msg.model_dump() for msg in request.messages],
            stream=request.stream
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"API调用失败: {str(e)}")

    async def event_generator():
        if request.stream:
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield {
                        "event": "message",
                        "data": json.dumps({'content': chunk.choices[0].delta.content})
                    }
            yield {"event": "message", "data": json.dumps({'content': '[DONE]'})}
        else:
            yield {
                "event": "message",
                "data": json.dumps({'content': response.choices[0].message.content})
            }
            yield {"event": "message", "data": json.dumps({'content': '[DONE]'})}

    return EventSourceResponse(event_generator())


@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {"status": "healthy", "message": "Chat CLI Backend is running"}


def run_server(host: str = "127.0.0.1", port: int = 8000):
    """启动服务器"""
    uvicorn.run(app, host=host, port=port, log_level="warning")


if __name__ == "__main__":
    run_server()
