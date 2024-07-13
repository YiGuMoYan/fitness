import datetime
import queue
import threading
from enum import Enum

from colorama import init, Fore, Style


class State(Enum):
    INFO = "[INFO]"
    ERROR = "[ERROR]"
    WARNING = "[WARNING]"
    SUCCESS = "[SUCCESS]"


class Logger:
    """
    日志
    """

    def __init__(self):
        """
        日志
        """
        self.name_width = 25
        self.state_width = 10
        self.print_queue = queue.Queue()
        init(autoreset=True)

        threading.Thread(target=self.print).start()

    @staticmethod
    def get_current_time() -> str:
        """
        获取当前时间
        @return: 当前时间
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_common_msg(self, name, msg) -> str:
        """
        获取通用消息
        @param name: 日志昵称
        @param msg: 消息
        @return: 通用消息
        """
        return f"[{self.get_current_time()}] {name:>{self.name_width}}: {msg}"

    def info(self, name, msg) -> None:
        """
        输出info日志
        @param name: 日志昵称
        @param msg: 消息
        """
        self.print_queue.put(f"{State.INFO.value:<{self.state_width}} {self.get_common_msg(name, msg)}")

    def error(self, name, msg) -> None:
        """
        输出error日志
        @param name: 日志昵称
        @param msg: 消息
        """
        self.print_queue.put(
            f"{Fore.RED}{State.ERROR.value:<{self.state_width}}{Style.RESET_ALL} {self.get_common_msg(name, msg)}")

    def warning(self, name, msg) -> None:
        """
        输出warning日志
        @param name: 日志昵称
        @param msg: 消息
        """
        self.print_queue.put(
            f"{Fore.YELLOW}{State.WARNING.value:<{self.state_width}}{Style.RESET_ALL} {self.get_common_msg(name, msg)}")

    def success(self, name, msg) -> None:
        """
        输出success日志
        @param name: 日志昵称
        @param msg: 消息
        """
        self.print_queue.put(
            f"{Fore.GREEN}{State.SUCCESS.value:<{self.state_width}}{Style.RESET_ALL} {self.get_common_msg(name, msg)}")

    def print(self) -> None:
        """
        打印日志
        """
        while True:
            print(self.print_queue.get())
            self.print_queue.task_done()


logger = Logger()
