#!/usr/bin/env python3

import json

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status}\n"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, status):
        task = Task(title, description, status)
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"Task {i}:\n{task}")

    def edit_task(self, task_index, title, description, status):
        task = self.tasks[task_index - 1]
        task.title = title
        task.description = description
        task.status = status

    def delete_task(self, task_index):
        del self.tasks[task_index - 1]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [{"title": task.title, "description": task.description, "status": task.status} for task in self.tasks]
            json.dump(tasks_data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task["title"], task["description"], task["status"]) for task in tasks_data]
        except FileNotFoundError:
            pass

# Пример использования
task_manager = TaskManager()
task_manager.load_from_file("tasks.json")

while True:
    print("\n1. Добавить задачу")
    print("2. Просмотреть задачи")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("5. Сохранить задачи в файл")
    print("6. Выйти")

    choice = input("Выберите действие (1-6): ")

    if choice == "1":
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        status = input("Введите статус задачи: ")
        task_manager.add_task(title, description, status)
    elif choice == "2":
        task_manager.view_tasks()
    elif choice == "3":
        task_index = int(input("Введите номер задачи для редактирования: "))
        title = input("Введите новое название задачи: ")
        description = input("Введите новое описание задачи: ")
        status = input("Введите новый статус задачи: ")
        task_manager.edit_task(task_index, title, description, status)
    elif choice == "4":
        task_index = int(input("Введите номер задачи для удаления: "))
        task_manager.delete_task(task_index)
    elif choice == "5":
        task_manager.save_to_file("tasks.json")
        print("Задачи сохранены в файл.")
    elif choice == "6":
        task_manager.save_to_file("tasks.json")
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите от 1 до 6.")
