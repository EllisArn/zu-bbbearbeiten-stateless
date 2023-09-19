import datetime
import operator
from dataclasses import dataclass

todos = []


@dataclass
class Item:
    text: str
    date: datetime
    isCompleted: bool = False


def oneWeekFromToday():
    today = datetime.datetime.now()
    oneWeek = datetime.timedelta(weeks=1)
    return today + oneWeek


def add(text, date=None):
    text = text.replace("b", "bbb").replace("B", "Bbb")

    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    todos.append(Item(text, date))
    todos.sort(key=operator.attrgetter("date"))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted
