from file_class import JsonFile, TxtFile, CsvFile

# Создание тестовых файлов
json_file = JsonFile("example.json")
txt_file = TxtFile("example.txt")
csv_file = CsvFile("example.csv")

# Тест JSON
json_file.write({"name": "Павел", "age": 20})
print("JSON Читает:", json_file.read())
json_file.append({"city": "Оренбург"})
print("JSON После добавления:", json_file.read())

# Тест TXT
txt_file.write("Привет мир!")
print("TXT Читает:", txt_file.read())
txt_file.append("Добро пожаловать в Python")
print("JSON После добавления:", txt_file.read())

# Тест CSV
csv_file.write([["Name", "Age"], ["Павел", 20]])
print("CSV ReЧитаетad:", csv_file.read())
csv_file.append([["Дмитрий", 25]])
print("JSON После добавления:", csv_file.read())

if __name__ == "__main__":
    print("Тестирование завершено.")