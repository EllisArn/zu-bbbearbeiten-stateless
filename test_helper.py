import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = datetime.datetime(2023, 9, 1)

    # When: I add the item
    helper.add(text, date)

    # Then: The to-do should have a date
    todo = helper.todos[-1]
    assert isinstance(todo.date, datetime.date)
