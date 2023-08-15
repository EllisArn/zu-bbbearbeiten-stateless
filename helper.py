from dataclasses import dataclass

# Die Daten werden in "Items" gespeichert
items = []

@dataclass
class Item:
    text: str
    isCompleted: bool = False

# Ver-BBB-isierung
def add(text):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text))

# Hier werden alle Items zurückgegeben
def get_all():
    return items

# Hier wird ein Item zurückgegeben
def get(index):
    return items[index]

# Hier wird ein Item als "erledigt" oder "nicht erledigt" markiert
def update(index):
    items[index].isCompleted = not items[index].isCompleted
