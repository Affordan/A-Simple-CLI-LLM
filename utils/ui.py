"""
工具模块 - 帮助信息和UI显示
"""
from colorama import Fore, Style


def show_help():
    """显示chat CLI的使用指令"""
    help_text = f"""
{Fore.CYAN}📱 Chat CLI - 智能聊天客户端{Style.RESET_ALL}
{Fore.YELLOW}==========================================={Style.RESET_ALL}

{Fore.GREEN}可用命令：{Style.RESET_ALL}
  {Fore.BLUE}chat start{Style.RESET_ALL}     - 启动交互式聊天会话
  {Fore.BLUE}chat server{Style.RESET_ALL}    - 仅启动后端服务器
  {Fore.BLUE}chat help{Style.RESET_ALL}      - 显示此帮助信息
  {Fore.BLUE}chat --help{Style.RESET_ALL}    - 显示详细帮助

{Fore.GREEN}交互式聊天中的命令：{Style.RESET_ALL}
  {Fore.MAGENTA}/help{Style.RESET_ALL}        - 显示聊天中的帮助
  {Fore.MAGENTA}/clear{Style.RESET_ALL}       - 清空聊天历史
  {Fore.MAGENTA}/model{Style.RESET_ALL}       - 切换AI模型
  {Fore.MAGENTA}/exit{Style.RESET_ALL}        - 退出聊天
  {Fore.MAGENTA}/quit{Style.RESET_ALL}        - 退出聊天

{Fore.GREEN}示例：{Style.RESET_ALL}
  {Fore.YELLOW}chat start{Style.RESET_ALL}              开始聊天
  {Fore.YELLOW}chat start --model gpt-4{Style.RESET_ALL} 使用指定模型开始聊天

{Fore.RED}注意：首次使用请确保已设置 DEEPSEEK_API_KEY 环境变量{Style.RESET_ALL}
"""
    print(help_text)


def show_chat_header(model: str):
    """显示聊天界面头部信息"""
    print(Fore.CYAN + f"📱 Chat CLI - 使用模型: {model}" + Style.RESET_ALL)
    print(Fore.CYAN + "==========================================" + Style.RESET_ALL)
    print(Fore.GREEN + "开始聊天！输入消息或使用以下命令：" + Style.RESET_ALL)
    print(Fore.MAGENTA + "/help - 显示帮助 | /clear - 清空历史 | /model - 切换模型 | /exit - 退出" + Style.RESET_ALL)
    print(Fore.CYAN + "==========================================" + Style.RESET_ALL)


def show_chat_help():
    """显示聊天中的帮助信息"""
    help_text = f"""
{Fore.CYAN}聊天中可用命令：{Style.RESET_ALL}
{Fore.MAGENTA}/help{Style.RESET_ALL}  - 显示此帮助
{Fore.MAGENTA}/clear{Style.RESET_ALL} - 清空聊天历史
{Fore.MAGENTA}/model{Style.RESET_ALL} - 切换AI模型
{Fore.MAGENTA}/exit{Style.RESET_ALL}  - 退出聊天
{Fore.MAGENTA}/quit{Style.RESET_ALL}  - 退出聊天
"""
    print(help_text)


def print_system_message(message: str):
    """打印系统消息"""
    print(Fore.YELLOW + f"[系统] {message}" + Style.RESET_ALL)


def print_error_message(message: str):
    """打印错误消息"""
    print(Fore.RED + f"[错误] {message}" + Style.RESET_ALL)


def print_success_message(message: str):
    """打印成功消息"""
    print(Fore.GREEN + f"[系统] {message}" + Style.RESET_ALL)
