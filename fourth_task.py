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
        if self.choose_source == 'telegram':
            return TelegramParser(self.message)
        elif self.choose_source == 'slack':
            return SlackParser(self.message)
        elif self.choose_source == 'mattermost':
            return MattermostParser(self.message)
        else:
            raise ValueError("Неизвестный тип источника")
