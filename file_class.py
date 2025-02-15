from abc import ABC, abstractmethod
import json
import csv




class AbstractFile(ABC):
    """Абстрактный класс для работы с файлами"""

    def __init__(self, file_path: str) -> None:
        """Инициализация с указанием пути к файлу"""
        self.file_path = file_path

    @abstractmethod
    def read(self) -> str:
        """Чтение данных из файла"""
        pass

    @abstractmethod
    def write(self, data: str) -> None:
        """Запись данных в файл (перезапись)"""
        pass

    @abstractmethod
    def append(self, data: str) -> None:
        """Добавление данных в файл (без удаления существующего)"""
        pass
    
class JsonFile(AbstractFile):
    """Класс для работы с JSON-файлами"""
    def read(self):
        """Чтение данных из JSON-файла"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return {}

    def write(self, data):
        """Запись данных в JSON-файл (перезапись)"""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def append(self, data):
        """Добавление данных в JSON-файл"""
        existing_data = self.read()
        if isinstance(existing_data, dict) and isinstance(data, dict):
            existing_data.update(data)
        elif isinstance(existing_data, list) and isinstance(data, list):
            existing_data.extend(data)
        else:
            existing_data = data

        self.write(existing_data)

class TxtFile(AbstractFile):
    """Класс для работы с TXT-файлами"""

    def read(self):
        """Чтение данных из TXT-файла"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def write(self, data):
        """Запись данных в TXT-файл (перезапись)"""
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(str(data))

    def append(self, data):
        """Добавление данных в TXT-файл"""
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write("\n" + str(data))


class CsvFile(AbstractFile):
    """Класс для работы с CSV-файлами"""

    def read(self):
        """Чтение данных из CSV-файла"""
        try:
            with open(self.file_path, newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                return [row for row in reader]
        except FileNotFoundError:
            return []

    def write(self, data):
        """Запись данных в CSV-файл (перезапись)"""
        with open(self.file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def append(self, data):
        """Добавление данных в CSV-файл"""
        with open(self.file_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
