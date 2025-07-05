"""
前端CLI - 交互式聊天功能
"""
import time
from multiprocessing import Process
from colorama import Fore, Style
from typing import List, Dict

from backend.server import run_server
from utils.api_client import send_chat_request, check_server_health
from utils.ui import (
    show_chat_header,
    show_chat_help,
    print_system_message,
    print_error_message,
    print_success_message
)


def start_server_process() -> Process:
    """启动后端服务器进程"""
    server_process = Process(target=run_server)
    print_system_message("正在启动后端服务器...")
    server_process.start()
    time.sleep(2)  # 等待服务器启动

    if not server_process.is_alive():
        print_error_message("服务器启动失败，请检查端口是否被占用")
        return None

    # 检查服务器健康状态
    if not check_server_health():
        print_error_message("服务器健康检查失败")
        server_process.terminate()
        return None

    print_success_message("服务器已就绪")
    return server_process


def interactive_chat(model: str = "deepseek-chat", stream: bool = True):
    """
    交互式聊天会话

    Args:
        model: AI模型名称
        stream: 是否启用流式响应
    """
    messages = []
    current_model = model

    show_chat_header(current_model)

    while True:
        try:
            user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL).strip()

            if not user_input:
                continue

            # 处理命令
            if user_input.lower() in ["/exit", "/quit"]:
                break
            elif user_input.lower() == "/help":
                show_chat_help()
                continue
            elif user_input.lower() == "/clear":
                messages = []
                print_system_message("聊天历史已清空")
                continue
            elif user_input.lower() == "/model":
                print(Fore.CYAN + f"当前模型: {current_model}" + Style.RESET_ALL)
                new_model = input(Fore.CYAN + "输入新模型名称 (直接回车保持不变): " + Style.RESET_ALL).strip()
                if new_model:
                    current_model = new_model
                    print_success_message(f"已切换到模型: {current_model}")
                continue

            # 正常聊天消息
            messages.append({"role": "user", "content": user_input})
            assistant_response = send_chat_request(messages, current_model, stream)

            if assistant_response:
                messages.append({"role": "assistant", "content": assistant_response})

        except (KeyboardInterrupt, EOFError):
            break

    print_system_message("退出聊天会话")


def chat_with_prompt(prompt: str, model: str = "deepseek-chat", stream: bool = True):
    """
    单次问答模式

    Args:
        prompt: 用户问题
        model: AI模型名称
        stream: 是否启用流式响应
    """
    messages = [{"role": "user", "content": prompt}]
    send_chat_request(messages, model, stream)
