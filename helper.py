from dataclasses import dataclass

# Die Daten werden in "todos" gespeichert
todos = []

@dataclass
class Todo:
    title: str
    isCompleted: bool = False

# Ver-BBB-isierung
def add(title):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    todos.append(Todo(title))

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
