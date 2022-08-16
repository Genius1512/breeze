from datetime import datetime
from termcolor import colored


class Logger:
    def __init__(self, name: str) -> None:
        self.__name = name

    def log(self, msg: str) -> None:
        print(
            colored(
                self.__get_logging_string(
                    msg, "LOG"
                ),
                "white",
            )
        )

    def warn(self, msg: str) -> None:
        print(
            colored(
                self.__get_logging_string(
                    msg, "WARN"
                ),
                "yellow",
            )
        )

    def error(self, msg: str) -> None:
        print(
            colored(
                self.__get_logging_string(
                    msg, "ERROR"
                ),
                "red",
            )
        )

    def success(self, msg: str) -> None:
        print(
            colored(
                self.__get_logging_string(
                    msg, "SUCCESS"
                ),
                "green",
            )
        )

    def __get_logging_string(
        self, msg: str, type_: str
    ) -> str:
        time_stamp = datetime.now().strftime(
            "%H:%M:%S"
        )
        return f"[{type_}]({time_stamp}) {self.__name}: {msg}"

    @property
    def name(self) -> str:
        return self.__name
