import csv
import datetime
import io
from dataclasses import dataclass

todos = []


@dataclass
class Todo:
    title: str
    date: datetime
    category: str
    description: str
    isCompleted: bool = False


def oneWeekFromToday():
    today = datetime.datetime.now()
    oneWeek = datetime.datetime(weeks=1)
    return today + oneWeek


def add(title, date=None, category=None, description=None):
    title = title.replace("b", "bbb").replace("B", "Bbb")
    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")

    if category is None:
        category = "default"

    if description is None:
        description = ""
    todos.append(Todo(title, date, category, description))
    todos.sort(key=lambda x: (x.date, x.category))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted


def get_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Titel", "Datum", "Kategorie", "Beschreibung", "Erledigt?"])
    for todo in todos:
        writer.writerow(
            [
                todo.title,
                todo.date.strftime("%d.%m.%Y"),
                todo.category,
                todo.description,
                "x" if todo.isCompleted else "o",
            ]
        )
    return output.getvalue()
