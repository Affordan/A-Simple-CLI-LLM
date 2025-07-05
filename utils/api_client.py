"""
工具模块 - API请求处理
"""
import json
import requests
from colorama import Fore, Style
from typing import List, Dict, Optional


def send_chat_request(
    messages: List[Dict],
    model: str,
    stream: bool = True,
    api_url: str = "http://127.0.0.1:8000/chat"
) -> Optional[str]:
    """
    发送聊天请求到后端API

    Args:
        messages: 消息列表
        model: 模型名称
        stream: 是否流式响应
        api_url: API地址

    Returns:
        完整的AI响应内容，失败时返回None
    """
    print(Fore.BLUE + "AI: " + Style.RESET_ALL, end="")
    full_response = ""
    payload = {"messages": messages, "stream": stream, "model": model}

    try:
        with requests.post(api_url, json=payload, stream=stream, timeout=120) as response:
            response.raise_for_status()

            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data:'):
                        json_str = decoded_line[5:].strip()
                        try:
                            data = json.loads(json_str)
                            content = data.get("content", "")
                            if content == "[DONE]":
                                break
                            print(content, end="", flush=True)
                            full_response += content
                        except json.JSONDecodeError:
                            continue

        print()  # 换行
        return full_response

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"\n[错误] 无法连接到服务器: {e}" + Style.RESET_ALL)
        return None


def check_server_health(api_url: str = "http://127.0.0.1:8000") -> bool:
    """
    检查服务器健康状态

    Args:
        api_url: API基础地址

    Returns:
        服务器是否健康
    """
    try:
        response = requests.get(f"{api_url}/health", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
