from abc import ABC, abstractmethod
from dataclasses import dataclass


class Parser(ABC):

    @abstractmethod
    def choose_sender(self):
        # получаем отправителя сообщения
        pass

    @abstractmethod
    def choose_text(self):
        # получаем текст сообщения
        pass

    @abstractmethod
    def choose_time(self):
        # получаем время отправки
        pass

    @abstractmethod
    def choose_source(self):
        # получаем источник сообщения
        pass


@dataclass
class TelegramParser(Parser):
    message: dict
    unified_message = {}

    def choose_sender(self):
        # получаем отправителя сообщения
        pass

    def choose_text(self):
        # получаем текст сообщения
        pass

    def choose_time(self):
        # получаем время отправки
        pass

    def choose_source(self):
        # получаем источник сообщения
        pass


@dataclass
class SlackParser(Parser):
    message: dict
    unified_message = {}

    def choose_sender(self):
        # получаем отправителя сообщения
        pass

    def choose_text(self):
        # получаем текст сообщения
        pass

    def choose_time(self):
        # получаем время отправки
        pass

    def choose_source(self):
        # получаем источник сообщения
        pass


@dataclass
class MattermostParser(Parser):
    message: dict
    unified_message = {}

    def choose_sender(self):
        # получаем отправителя сообщения
        pass

    def choose_text(self):
        # получаем текст сообщения
        pass

    def choose_time(self):
        # получаем время отправки
        pass

    def choose_source(self):
        # получаем источник сообщения
        pass


@dataclass
class ParserFactory:
    message: dict

    def choose_source(self):
        # получаем источник сообщения
        pass

    def create_parser(self):
        # в зависимости от источника сообщения вызываем нужный парсер
        # а то что мне в словарь придется добавлять новый класс парсера и название мессенджера - это норм?
        PARSER_MAP = {
            'telegram': TelegramParser,
            'slack': SlackParser,
            'mattermost': MattermostParser,
        }
        source_type = self.choose_source()
        parser_class = PARSER_MAP.get(source_type)
        if not parser_class:
            raise ValueError("Неизвестный тип источника")
        return parser_class(self.message)
