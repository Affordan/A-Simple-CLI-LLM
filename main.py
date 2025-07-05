"""
Chat CLI - 智能聊天客户端
"""
import sys
import typer
from multiprocessing import Process
from colorama import init
from typing_extensions import Annotated

from backend.server import run_server
from frontend.chat import interactive_chat, chat_with_prompt, start_server_process
from utils.ui import show_help, print_error_message, print_success_message

# 初始化colorama
init()

# 创建Typer应用
app = typer.Typer(
    add_completion=False,
    help="一个可以同时启动后端服务并与之交互的智能聊天客户端。"
)


@app.command()
def start(
    model: Annotated[str, typer.Option(help="选择要使用的模型")] = "deepseek-chat",
    stream: Annotated[bool, typer.Option("--stream/--no-stream", help="启用或禁用流式响应")] = True
):
    """启动交互式聊天会话"""
    server_process = start_server_process()
    if not server_process:
        return

    try:
        interactive_chat(model, stream)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        print_success_message("正在关闭服务器...")
        if server_process.is_alive():
            server_process.terminate()
            server_process.join()
        print_success_message("程序已退出。再见！")


@app.command()
def server(
    host: Annotated[str, typer.Option(help="服务器主机地址")] = "127.0.0.1",
    port: Annotated[int, typer.Option(help="服务器端口")] = 8000
):
    """仅启动后端服务器"""
    print_success_message(f"启动FastAPI服务器在 http://{host}:{port}")
    print_success_message("按 Ctrl+C 停止服务器")
    try:
        run_server(host, port)
    except KeyboardInterrupt:
        print_success_message("服务器已停止")


@app.command()
def help():
    """显示详细的使用帮助"""
    show_help()


@app.command(name="chat")
def chat_command(
    prompt: Annotated[str, typer.Argument(
        help="要直接发送给模型的单个问题。如果未提供，则进入交互模式。",
        show_default=False
    )] = None,
    model: Annotated[str, typer.Option(help="选择要使用的模型。")] = "deepseek-chat",
    stream: Annotated[bool, typer.Option("--stream/--no-stream", help="启用或禁用流式响应。")] = True
):
    """发送消息给AI（需要服务器已运行）或启动完整会话"""
    server_process = start_server_process()
    if not server_process:
        return

    try:
        if prompt:
            chat_with_prompt(prompt, model, stream)
        else:
            interactive_chat(model, stream)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        print_success_message("正在关闭服务器...")
        if server_process.is_alive():
            server_process.terminate()
            server_process.join()
        print_success_message("程序已退出。再见！")


def main_entry():
    """程序入口点，显示帮助信息然后运行CLI"""
    if len(sys.argv) == 1:  # 只有程序名，没有其他参数
        show_help()
        return
    app()


if __name__ == "__main__":
    main_entry()
