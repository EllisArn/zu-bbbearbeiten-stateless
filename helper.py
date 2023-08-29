from dataclasses import dataclass
import datetime

# Die Daten werden in "todos" gespeichert
todos = []

@dataclass
class Todo:
    title: str
    date: datetime.date
    isCompleted: bool = False

# Ver-BBB-isierung
def add(title, date):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    todos.append(Todo(title, date))

# Hier werden alle todos zurückgegeben
def get_all():
    print(todos)
    return todos

# Hier wird ein Item zurückgegeben
def get(index):
    return todos[index]

# Hier wird ein Item als "erledigt" oder "nicht erledigt" markiert
def update(index):
    todos[index].isCompleted = not todos[index].isCompleted
