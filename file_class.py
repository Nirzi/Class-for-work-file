from abc import ABC, abstractmethod


class AbstractFile(ABC):
    """Абстрактный класс для работы с файлами"""

    def __init__(self, file_path: str):
        """Инициализация с указанием пути к файлу"""
        self.file_path = file_path

    @abstractmethod
    def read(self):
        """Чтение данных из файла"""
        pass

    @abstractmethod
    def write(self, data):
        """Запись данных в файл (перезапись)"""
        pass

    @abstractmethod
    def append(self, data):
        """Добавление данных в файл (без удаления существующего)"""
        pass
